import unreal


TARGET_BLUEPRINTS = [
    "/Game/FirstPerson/Blueprints/BP_FirstPersonGameMode",
    "/Game/FirstPerson/Blueprints/BP_FirstPersonCharacter",
    "/Game/FirstPerson/Blueprints/BP_FirstPersonPlayerController",
    "/Game/FirstPerson/FirstPerson/Blueprints/BP_FirstPersonGameMode",
    "/Game/FirstPerson/FirstPerson/Blueprints/BP_FirstPersonCharacter",
    "/Game/FirstPerson/FirstPerson/Blueprints/BP_FirstPersonPlayerController",
]

KEYWORDS = (
    "bot",
    "npc",
    "ai",
    "spawn",
    "respawn",
    "wave",
    "enemy",
    "score",
    "goal",
    "time",
    "match",
    "round",
    "zone",
)


def inspect_blueprint(path: str):
    bp = unreal.EditorAssetLibrary.load_asset(path)
    if not bp:
        return

    unreal.log_warning(f"PIPELINE_BP_FOUND {path}")
    cls = bp.generated_class()
    if not cls:
        unreal.log_warning(f"PIPELINE_BP_NO_CLASS {path}")
        return

    cdo = unreal.get_default_object(cls)
    names = sorted([n for n in dir(cdo) if not n.startswith("_")])
    likely = [n for n in names if any(k in n.lower() for k in KEYWORDS)]
    unreal.log_warning(f"PIPELINE_BP_LIKELY_COUNT {path} {len(likely)}")

    for name in likely[:180]:
        try:
            value = cdo.get_editor_property(name)
            unreal.log_warning(f"PIPELINE_PROP {path} {name}={value}")
        except Exception as ex:
            unreal.log_warning(f"PIPELINE_PROP_SKIP {path} {name}: {ex}")


def main():
    for path in TARGET_BLUEPRINTS:
        inspect_blueprint(path)
    unreal.log_warning("PIPELINE_INSPECT_COMPLETE")


if __name__ == "__main__":
    main()
