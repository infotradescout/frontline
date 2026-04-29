#pragma once

#include "CoreMinimal.h"
#include "GameFramework/GameModeBase.h"
#include "FrontlineBRGameState.h"
#include "FrontlineBRGameMode.generated.h"

UCLASS(BlueprintType)
class FRONTLINEWARFARE_API AFrontlineBRGameMode : public AGameModeBase
{
    GENERATED_BODY()

public:
    AFrontlineBRGameMode();

    virtual void BeginPlay() override;
    virtual void PostLogin(APlayerController* NewPlayer) override;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Match")
    float WarmupSeconds;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Match")
    float LiveMatchSeconds;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Match")
    float RestartDelaySeconds;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Match")
    bool bAnnounceWinnerOnScreen;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Match")
    float WinnerAnnouncementSeconds;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Bots")
    int32 TargetBotCount;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Bots")
    float BotSpawnRadius;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category = "Bots")
    bool bSpawnBotsAtBeginPlay;

private:
    FTimerHandle TickMatchTimerHandle;
    float ServerPhaseTimeRemaining;

    void SpawnInitialBots();

    void EnterPhase(EFrontlineMatchPhase NewPhase);
    void TickMatchPhase();
    void RefreshAliveCounts(AFrontlineBRGameState* BRGameState, APawn*& OutLastAlivePawn) const;
    void EndMatchWithWinner(APawn* WinnerPawn, const FString& Reason);
    FString BuildWinnerLabel(const APawn* WinnerPawn) const;
};
