import unreal


CANDIDATE_MAPS = [
    "/Game/Variant_Shooter/Lvl_ArenaShooter",
    "/Game/Variant_Shooter_BP/Lvl_Shooter",
    "/Game/Variant_Shooter_Std/Lvl_Shooter",
    "/Game/FirstPerson/Lvl_FirstPerson",
    "/Game/FirstPerson/FirstPerson/Lvl_FirstPerson",
]

CANDIDATE_GAMEMODES = [
    "/Game/Variant_Shooter/Blueprints/BP_ShooterGameMode",
    "/Game/Variant_Shooter_BP/Blueprints/BP_ShooterGameMode",
    "/Game/Variant_Shooter_Std/Blueprints/BP_ShooterGameMode",
    "/Game/FirstPerson/Blueprints/BP_FirstPersonGameMode",
    "/Game/FirstPerson/FirstPerson/Blueprints/BP_FirstPersonGameMode",
]

CHECK_PROPS = [
    "goal_score",
    "time_limit",
    "num_bots",
    "minimum_respawn_delay",
    "inactive_player_state_life_span",
    "max_inactive_players",
]


def load_first(paths: list[str]):
    for path in paths:
        if not unreal.EditorAssetLibrary.does_asset_exist(path):
            continue
        asset = unreal.EditorAssetLibrary.load_asset(path)
        if asset is not None:
            unreal.log_warning(f"BR_VERIFY_FOUND {path}")
            return path, asset
    return None, None


def _is_bot_spawner(actor):
    cls_name = actor.get_class().get_name().lower()
    actor_name = actor.get_name().lower()
    tokens = ("spawner", "spawn")
    bot_tokens = ("bot", "npc", "shooter")
    return any(t in cls_name for t in tokens) and (
        any(b in cls_name for b in bot_tokens) or any(b in actor_name for b in bot_tokens)
    )


def _is_spawn_actor(actor):
    cls_name = actor.get_class().get_name().lower()
    actor_name = actor.get_name().lower()
    if "playerstart" in cls_name:
        return True
    if "targetpoint" in cls_name:
        return True
    if "spawn" in cls_name or "spawn" in actor_name:
        return True
    return False


def verify():
    gm_path, gm_bp = load_first(CANDIDATE_GAMEMODES)
    if gm_bp and gm_bp.generated_class():
        cdo = unreal.get_default_object(gm_bp.generated_class())
        for prop in CHECK_PROPS:
            try:
                value = cdo.get_editor_property(prop)
                unreal.log_warning(f"BR_VERIFY_GM {prop}={value}")
            except Exception as ex:
                unreal.log_warning(f"BR_VERIFY_GM_MISSING {prop}: {ex}")
    else:
        unreal.log_warning("BR_VERIFY_GM_NOT_FOUND")

    map_path, _ = load_first(CANDIDATE_MAPS)
    if not map_path:
        unreal.log_error("BR_VERIFY_MAP_NOT_FOUND")
        raise SystemExit(1)

    world = unreal.EditorLoadingAndSavingUtils.load_map(map_path)
    if not world:
        unreal.log_error(f"BR_VERIFY_MAP_LOAD_FAILED {map_path}")
        raise SystemExit(1)

    actors = unreal.EditorLevelLibrary.get_all_level_actors()
    spawners = [a for a in actors if _is_bot_spawner(a)]
    spawn_actors = [a for a in actors if _is_spawn_actor(a)]
    elevated_spawns = [a for a in spawn_actors if a.get_actor_location().z > 100.0]
    nav_bounds = [a for a in actors if a.get_class().get_name() == "NavMeshBoundsVolume"]
    unreal.log_warning(f"BR_VERIFY_SPAWNERS {len(spawners)}")
    unreal.log_warning(f"BR_VERIFY_SPAWN_ACTORS {len(spawn_actors)}")
    unreal.log_warning(f"BR_VERIFY_ELEVATED_SPAWNS {len(elevated_spawns)}")
    for actor in elevated_spawns:
        loc = actor.get_actor_location()
        unreal.log_warning(
            f"BR_VERIFY_ELEVATED {actor.get_name()} CLASS={actor.get_class().get_name()} "
            f"LOC=({loc.x:.1f},{loc.y:.1f},{loc.z:.1f})"
        )
    if len(spawners) == 0:
        unreal.log_warning(
            "BR_VERIFY_RUNTIME_BOTS_MODE No editor spawner actors found; "
            "runtime bot spawn pipeline is likely blueprint-driven."
        )
    unreal.log_warning(f"BR_VERIFY_NAV_BOUNDS {len(nav_bounds)}")
    unreal.log_warning("BR_VERIFY_COMPLETE")


if __name__ == "__main__":
    verify()
