#include "FrontlineBRGameState.h"
#include "Net/UnrealNetwork.h"

AFrontlineBRGameState::AFrontlineBRGameState()
{
    bReplicates = true;
    MatchPhase = EFrontlineMatchPhase::Warmup;
    PhaseTimeRemaining = 0.0f;
    AliveHumanPlayers = 0;
    AliveBots = 0;
    AliveTotal = 0;
    WinnerLabel = TEXT("");
}

void AFrontlineBRGameState::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const
{
    Super::GetLifetimeReplicatedProps(OutLifetimeProps);

    DOREPLIFETIME(AFrontlineBRGameState, MatchPhase);
    DOREPLIFETIME(AFrontlineBRGameState, PhaseTimeRemaining);
    DOREPLIFETIME(AFrontlineBRGameState, AliveHumanPlayers);
    DOREPLIFETIME(AFrontlineBRGameState, AliveBots);
    DOREPLIFETIME(AFrontlineBRGameState, AliveTotal);
    DOREPLIFETIME(AFrontlineBRGameState, WinnerLabel);
}
