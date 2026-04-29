using UnrealBuildTool;

public class FrontlineWarfare : ModuleRules
{
    public FrontlineWarfare(ReadOnlyTargetRules Target) : base(Target)
    {
        PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;

        PublicDependencyModuleNames.AddRange(
            new string[]
            {
                "Core",
                "CoreUObject",
                "Engine",
                "InputCore",
                "AIModule",
                "GameplayTasks",
                "NavigationSystem"
            }
        );
    }
}
