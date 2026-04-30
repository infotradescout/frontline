#include "FrontlineBRGameMode.h"

#include "AIController.h"
#include "Engine/Engine.h"
#include "EngineUtils.h"
#include "GameFramework/Character.h"
#include "GameFramework/CharacterMovementComponent.h"
#include "GameFramework/Pawn.h"
#include "GameFramework/PlayerController.h"
#include "GameFramework/PlayerState.h"
#include "GameFramework/PlayerStart.h"
#include "Kismet/GameplayStatics.h"
#include "NavigationSystem.h"
#include "UObject/ConstructorHelpers.h"
#include "TimerManager.h"

AFrontlineBRGameMode::AFrontlineBRGameMode()
{
    GameStateClass = AFrontlineBRGameState::StaticClass();

    // Force the intended first-person pawn instead of falling back to DefaultPawn (sphere).
    static ConstructorHelpers::FClassFinder<APawn> FPCharacterBP(
        TEXT("/Game/FirstPerson/Blueprints/BP_FirstPersonCharacter"));
    if (FPCharacterBP.Succeeded())
    {
        DefaultPawnClass = FPCharacterBP.Class;
    }

    WarmupSeconds = 10.0f;
    LiveMatchSeconds = 240.0f;
    RestartDelaySeconds = 10.0f;
    bAnnounceWinnerOnScreen = true;
    WinnerAnnouncementSeconds = 8.0f;
    TargetBotCount = 10;
    BotSpawnRadius = 1500.0f;
    bSpawnBotsAtBeginPlay = true;
    ServerPhaseTimeRemaining = 0.0f;
}

void AFrontlineBRGameMode::BeginPlay()
{
    Super::BeginPlay();

    if (UGameplayStatics::IsGamePaused(this))
    {
        UGameplayStatics::SetGamePaused(this, false);
        UE_LOG(LogTemp, Warning, TEXT("FrontlineBRGameMode: Cleared paused state on BeginPlay"));
    }

    UWorld* World = GetWorld();
    const FString WorldPackageName = (World && World->GetOutermost())
        ? World->GetOutermost()->GetName()
        : TEXT("<None>");

    // Guard against the known bad nested map path that can launch the wrong experience.
    if (WorldPackageName.Contains(TEXT("/Game/FirstPerson/FirstPerson/Lvl_FirstPerson")))
    {
        UE_LOG(
            LogTemp,
            Error,
            TEXT("FrontlineBRGameMode: Wrong map package loaded (%s). Redirecting to /Game/FirstPerson/Lvl_FirstPerson"),
            *WorldPackageName);

        UGameplayStatics::OpenLevel(this, FName(TEXT("/Game/FirstPerson/Lvl_FirstPerson")), true);
        return;
    }

    UE_LOG(
        LogTemp,
        Log,
        TEXT("FrontlineBRGameMode: BeginPlay Map=%s Package=%s DefaultPawnClass=%s"),
        *UGameplayStatics::GetCurrentLevelName(this, true),
        *WorldPackageName,
        *GetNameSafe(DefaultPawnClass));

    SpawnInitialBots();

    EnterPhase(EFrontlineMatchPhase::Warmup);
    GetWorldTimerManager().SetTimer(TickMatchTimerHandle, this, &AFrontlineBRGameMode::TickMatchPhase, 1.0f, true);
}

void AFrontlineBRGameMode::PostLogin(APlayerController* NewPlayer)
{
    Super::PostLogin(NewPlayer);

    if (!IsValid(NewPlayer))
    {
        return;
    }

    // Force game input focus in PIE to avoid sessions where camera and movement appear frozen.
    NewPlayer->SetIgnoreMoveInput(false);
    NewPlayer->SetIgnoreLookInput(false);
    NewPlayer->bShowMouseCursor = false;
    FInputModeGameOnly GameOnlyInputMode;
    GameOnlyInputMode.SetConsumeCaptureMouseDown(false);
    NewPlayer->SetInputMode(GameOnlyInputMode);

    APawn* Pawn = NewPlayer->GetPawn();
    if (!Pawn)
    {
        RestartPlayer(NewPlayer);
        Pawn = NewPlayer->GetPawn();
    }

    if (Pawn)
    {
        Pawn->EnableInput(NewPlayer);

        if (ACharacter* Character = Cast<ACharacter>(Pawn))
        {
            if (UCharacterMovementComponent* MoveComp = Character->GetCharacterMovement())
            {
                MoveComp->SetMovementMode(MOVE_Walking);
            }
        }
    }

    UE_LOG(
        LogTemp,
        Log,
        TEXT("FrontlineBRGameMode: PostLogin Controller=%s Pawn=%s PawnClass=%s IgnoreMove=%d IgnoreLook=%d"),
        *GetNameSafe(NewPlayer),
        *GetNameSafe(Pawn),
        Pawn ? *GetNameSafe(Pawn->GetClass()) : TEXT("None"),
        NewPlayer->IsMoveInputIgnored() ? 1 : 0,
        NewPlayer->IsLookInputIgnored() ? 1 : 0);

    if (!Pawn)
    {
        TWeakObjectPtr<APlayerController> WeakPC(NewPlayer);
        GetWorldTimerManager().SetTimerForNextTick([this, WeakPC]()
        {
            if (!WeakPC.IsValid())
            {
                return;
            }

            APawn* LatePawn = WeakPC->GetPawn();
            UE_LOG(
                LogTemp,
                Log,
                TEXT("FrontlineBRGameMode: PostLoginNextTick Controller=%s Pawn=%s PawnClass=%s"),
                *GetNameSafe(WeakPC.Get()),
                *GetNameSafe(LatePawn),
                LatePawn ? *GetNameSafe(LatePawn->GetClass()) : TEXT("None"));
        });
    }
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

    if (bAnnounceWinnerOnScreen)
    {
        const FString Announcement = FString::Printf(TEXT("Match Ended: %s"), *BRGameState->WinnerLabel);
        for (FConstPlayerControllerIterator It = GetWorld()->GetPlayerControllerIterator(); It; ++It)
        {
            if (APlayerController* PC = It->Get())
            {
                PC->ClientMessage(Announcement);
            }
        }

        if (GEngine)
        {
            GEngine->AddOnScreenDebugMessage(
                -1,
                WinnerAnnouncementSeconds,
                FColor::Yellow,
                Announcement,
                true,
                FVector2D(1.4f, 1.4f));
        }

        UE_LOG(LogTemp, Log, TEXT("FrontlineBRGameMode: %s"), *Announcement);
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
