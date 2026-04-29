#pragma once

#include "CoreMinimal.h"
#include "GameFramework/GameStateBase.h"
#include "FrontlineBRGameState.generated.h"

UENUM(BlueprintType)
enum class EFrontlineMatchPhase : uint8
{
    Warmup,
    Live,
    Ended
};

UCLASS(BlueprintType)
class FRONTLINEWARFARE_API AFrontlineBRGameState : public AGameStateBase
{
    GENERATED_BODY()

public:
    AFrontlineBRGameState();

    UPROPERTY(BlueprintReadOnly, Replicated, Category = "Match")
    EFrontlineMatchPhase MatchPhase;

    UPROPERTY(BlueprintReadOnly, Replicated, Category = "Match")
    float PhaseTimeRemaining;

    UPROPERTY(BlueprintReadOnly, Replicated, Category = "Match")
    int32 AliveHumanPlayers;

    UPROPERTY(BlueprintReadOnly, Replicated, Category = "Match")
    int32 AliveBots;

    UPROPERTY(BlueprintReadOnly, Replicated, Category = "Match")
    int32 AliveTotal;

    UPROPERTY(BlueprintReadOnly, Replicated, Category = "Match")
    FString WinnerLabel;

    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;
};
