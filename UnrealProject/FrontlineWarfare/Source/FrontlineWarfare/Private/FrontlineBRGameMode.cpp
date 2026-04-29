#include "FrontlineBRGameMode.h"

#include "AIController.h"
#include "EngineUtils.h"
#include "GameFramework/Pawn.h"
#include "GameFramework/PlayerController.h"
#include "GameFramework/PlayerState.h"
#include "GameFramework/PlayerStart.h"
#include "Kismet/GameplayStatics.h"
#include "NavigationSystem.h"
#include "TimerManager.h"

AFrontlineBRGameMode::AFrontlineBRGameMode()
{
    GameStateClass = AFrontlineBRGameState::StaticClass();

    WarmupSeconds = 10.0f;
    LiveMatchSeconds = 300.0f;
    RestartDelaySeconds = 8.0f;
    TargetBotCount = 8;
    BotSpawnRadius = 1500.0f;
    bSpawnBotsAtBeginPlay = true;
    ServerPhaseTimeRemaining = 0.0f;
}

void AFrontlineBRGameMode::BeginPlay()
{
    Super::BeginPlay();

    SpawnInitialBots();

    EnterPhase(EFrontlineMatchPhase::Warmup);
    GetWorldTimerManager().SetTimer(TickMatchTimerHandle, this, &AFrontlineBRGameMode::TickMatchPhase, 1.0f, true);
}

void AFrontlineBRGameMode::SpawnInitialBots()
{
    if (!bSpawnBotsAtBeginPlay || TargetBotCount <= 0 || !DefaultPawnClass)
    {
        return;
    }

    TArray<AActor*> PlayerStarts;
    UGameplayStatics::GetAllActorsOfClass(this, APlayerStart::StaticClass(), PlayerStarts);

    UNavigationSystemV1* NavSys = FNavigationSystem::GetCurrent<UNavigationSystemV1>(GetWorld());
    int32 Spawned = 0;

    for (int32 BotIdx = 0; BotIdx < TargetBotCount; ++BotIdx)
    {
        FVector BaseLocation = FVector::ZeroVector;
        if (PlayerStarts.Num() > 0)
        {
            BaseLocation = PlayerStarts[BotIdx % PlayerStarts.Num()]->GetActorLocation();
        }

        FVector SpawnLocation = BaseLocation;
        if (NavSys)
        {
            FNavLocation ReachableLocation;
            if (NavSys->GetRandomReachablePointInRadius(BaseLocation, BotSpawnRadius, ReachableLocation))
            {
                SpawnLocation = ReachableLocation.Location;
            }
        }

        SpawnLocation.Z += 50.0f;

        FActorSpawnParameters SpawnParams;
        SpawnParams.SpawnCollisionHandlingOverride = ESpawnActorCollisionHandlingMethod::AdjustIfPossibleButAlwaysSpawn;
        APawn* BotPawn = GetWorld()->SpawnActor<APawn>(DefaultPawnClass, SpawnLocation, FRotator::ZeroRotator, SpawnParams);
        if (!IsValid(BotPawn))
        {
            continue;
        }

        BotPawn->SpawnDefaultController();
        ++Spawned;
    }

    UE_LOG(LogTemp, Log, TEXT("FrontlineBRGameMode: Spawned %d/%d bots"), Spawned, TargetBotCount);
}

void AFrontlineBRGameMode::EnterPhase(EFrontlineMatchPhase NewPhase)
{
    AFrontlineBRGameState* BRGameState = GetGameState<AFrontlineBRGameState>();
    if (!BRGameState)
    {
        return;
    }

    BRGameState->MatchPhase = NewPhase;

    if (NewPhase == EFrontlineMatchPhase::Warmup)
    {
        ServerPhaseTimeRemaining = WarmupSeconds;
    }
    else if (NewPhase == EFrontlineMatchPhase::Live)
    {
        ServerPhaseTimeRemaining = LiveMatchSeconds;
    }
    else
    {
        ServerPhaseTimeRemaining = RestartDelaySeconds;
    }

    BRGameState->PhaseTimeRemaining = ServerPhaseTimeRemaining;
}

void AFrontlineBRGameMode::TickMatchPhase()
{
    AFrontlineBRGameState* BRGameState = GetGameState<AFrontlineBRGameState>();
    if (!BRGameState)
    {
        return;
    }

    APawn* LastAlivePawn = nullptr;
    RefreshAliveCounts(BRGameState, LastAlivePawn);

    if (BRGameState->MatchPhase == EFrontlineMatchPhase::Live && BRGameState->AliveTotal <= 1)
    {
        EndMatchWithWinner(LastAlivePawn, TEXT("LastAlive"));
        return;
    }

    ServerPhaseTimeRemaining = FMath::Max(0.0f, ServerPhaseTimeRemaining - 1.0f);
    BRGameState->PhaseTimeRemaining = ServerPhaseTimeRemaining;

    if (ServerPhaseTimeRemaining > 0.0f)
    {
        return;
    }

    if (BRGameState->MatchPhase == EFrontlineMatchPhase::Warmup)
    {
        EnterPhase(EFrontlineMatchPhase::Live);
        return;
    }

    if (BRGameState->MatchPhase == EFrontlineMatchPhase::Live)
    {
        EndMatchWithWinner(LastAlivePawn, TEXT("TimeCap"));
        return;
    }

    if (BRGameState->MatchPhase == EFrontlineMatchPhase::Ended)
    {
        const FString CurrentLevel = UGameplayStatics::GetCurrentLevelName(this, true);
        UGameplayStatics::OpenLevel(this, FName(*CurrentLevel), true);
    }
}

void AFrontlineBRGameMode::RefreshAliveCounts(AFrontlineBRGameState* BRGameState, APawn*& OutLastAlivePawn) const
{
    OutLastAlivePawn = nullptr;

    int32 HumanAlive = 0;
    int32 BotsAlive = 0;
    int32 TotalAlive = 0;

    for (TActorIterator<APawn> It(GetWorld()); It; ++It)
    {
        APawn* Pawn = *It;
        if (!IsValid(Pawn) || Pawn->IsActorBeingDestroyed())
        {
            continue;
        }

        // Living match participants should have a controller during active play.
        if (!IsValid(Pawn->GetController()))
        {
            continue;
        }

        ++TotalAlive;
        OutLastAlivePawn = Pawn;

        if (Pawn->GetController()->IsA<APlayerController>())
        {
            ++HumanAlive;
        }
        else if (Pawn->GetController()->IsA<AAIController>())
        {
            ++BotsAlive;
        }
    }

    BRGameState->AliveHumanPlayers = HumanAlive;
    BRGameState->AliveBots = BotsAlive;
    BRGameState->AliveTotal = TotalAlive;
}

void AFrontlineBRGameMode::EndMatchWithWinner(APawn* WinnerPawn, const FString& Reason)
{
    AFrontlineBRGameState* BRGameState = GetGameState<AFrontlineBRGameState>();
    if (!BRGameState || BRGameState->MatchPhase == EFrontlineMatchPhase::Ended)
    {
        return;
    }

    BRGameState->WinnerLabel = BuildWinnerLabel(WinnerPawn);
    if (BRGameState->WinnerLabel.IsEmpty())
    {
        BRGameState->WinnerLabel = FString::Printf(TEXT("No Winner (%s)"), *Reason);
    }

    EnterPhase(EFrontlineMatchPhase::Ended);
}

FString AFrontlineBRGameMode::BuildWinnerLabel(const APawn* WinnerPawn) const
{
    if (!IsValid(WinnerPawn) || !IsValid(WinnerPawn->GetController()))
    {
        return TEXT("");
    }

    const AController* Controller = WinnerPawn->GetController();
    if (const APlayerState* PlayerState = Controller->GetPlayerState<APlayerState>())
    {
        const FString PlayerName = PlayerState->GetPlayerName();
        if (!PlayerName.IsEmpty())
        {
            return FString::Printf(TEXT("%s Wins"), *PlayerName);
        }
    }

    if (Controller->IsA<AAIController>())
    {
        return TEXT("Bot Wins");
    }

    return TEXT("Player Wins");
}
