import unreal


CANDIDATE_MAPS = [
    "/Game/Variant_Shooter/Lvl_ArenaShooter",
    "/Game/Variant_Shooter_BP/Lvl_Shooter",
    "/Game/Variant_Shooter_Std/Lvl_Shooter",
    "/Game/FirstPerson/Lvl_FirstPerson",
    "/Game/FirstPerson/FirstPerson/Lvl_FirstPerson",
]


def load_first_map():
    for path in CANDIDATE_MAPS:
        asset = unreal.EditorAssetLibrary.load_asset(path)
        if asset is not None:
            return path
    return None


def main():
    map_path = load_first_map()
    if not map_path:
        unreal.log_error("INSPECT_NO_MAP_FOUND")
        raise SystemExit(1)

    world = unreal.EditorLoadingAndSavingUtils.load_map(map_path)
    if not world:
        unreal.log_error(f"INSPECT_FAILED_LOAD_MAP {map_path}")
        raise SystemExit(1)

    actors = unreal.EditorLevelLibrary.get_all_level_actors()
    unreal.log_warning(f"INSPECT_MAP {map_path}")
    unreal.log_warning(f"INSPECT_ACTOR_COUNT {len(actors)}")

    class_counts = {}
    for actor in actors:
        cls = actor.get_class().get_name()
        class_counts[cls] = class_counts.get(cls, 0) + 1

    for cls, count in sorted(class_counts.items(), key=lambda x: (-x[1], x[0]))[:120]:
        unreal.log_warning(f"INSPECT_CLASS {cls} COUNT={count}")

    keywords = ("bot", "npc", "ai", "spawn", "enemy", "shooter")
    for actor in actors:
        cls_name = actor.get_class().get_name().lower()
        actor_name = actor.get_name().lower()
        if any(k in cls_name for k in keywords) or any(k in actor_name for k in keywords):
            loc = actor.get_actor_location()
            unreal.log_warning(
                "INSPECT_CANDIDATE "
                f"NAME={actor.get_name()} CLASS={actor.get_class().get_name()} "
                f"LOC=({loc.x:.1f},{loc.y:.1f},{loc.z:.1f})"
            )

    unreal.log_warning("INSPECT_COMPLETE")


if __name__ == "__main__":
    main()
