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

# Apply these values only when a property exists on the chosen GameMode CDO.
GM_TARGETS = {
    "goal_score": 25,
    "time_limit": 12,
    "num_bots": 12,
    "minimum_respawn_delay": 2.0,
    "inactive_player_state_life_span": 120.0,
    "max_inactive_players": 32,
}

SPAWNER_POINTS = [
    unreal.Vector(-950.0, -950.0, 120.0),
    unreal.Vector(950.0, -950.0, 120.0),
    unreal.Vector(-950.0, 950.0, 120.0),
    unreal.Vector(950.0, 950.0, 120.0),
]


def load_first(paths: list[str]):
    for path in paths:
        asset = unreal.EditorAssetLibrary.load_asset(path)
        if asset is not None:
            unreal.log_warning(f"BR_APPLY_FOUND {path}")
            return path, asset
        unreal.log_warning(f"BR_APPLY_MISS {path}")
    return None, None


def tune_game_mode():
    gm_path, gm_bp = load_first(CANDIDATE_GAMEMODES)
    if not gm_bp:
        unreal.log_warning("BR_APPLY_NO_GAMEMODE_FOUND")
        return None

    gm_cls = gm_bp.generated_class()
    if not gm_cls:
        unreal.log_warning(f"BR_APPLY_GAMEMODE_NO_CLASS {gm_path}")
        return gm_path

    cdo = unreal.get_default_object(gm_cls)
    for prop, value in GM_TARGETS.items():
        try:
            old = cdo.get_editor_property(prop)
            cdo.set_editor_property(prop, value)
            new = cdo.get_editor_property(prop)
            unreal.log_warning(f"BR_APPLY_GM_SET {prop}: {old} -> {new}")
        except Exception as ex:
            unreal.log_warning(f"BR_APPLY_GM_SKIP {prop}: {ex}")

    saved = unreal.EditorAssetLibrary.save_loaded_asset(gm_bp)
    unreal.log_warning(f"BR_APPLY_GM_SAVE {saved} PATH={gm_path}")
    return gm_path


def _is_bot_spawner(actor):
    cls_name = actor.get_class().get_name().lower()
    actor_name = actor.get_name().lower()
    tokens = ("spawner", "spawn")
    bot_tokens = ("bot", "npc", "shooter")
    return any(t in cls_name for t in tokens) and (
        any(b in cls_name for b in bot_tokens) or any(b in actor_name for b in bot_tokens)
    )


def ensure_nav_bounds(world):
    actors = unreal.EditorLevelLibrary.get_all_level_actors()
    nav_bounds = [a for a in actors if a.get_class().get_name() == "NavMeshBoundsVolume"]
    if not nav_bounds:
        created = unreal.EditorLevelLibrary.spawn_actor_from_class(
            unreal.NavMeshBoundsVolume,
            unreal.Vector(0.0, 0.0, 200.0),
            unreal.Rotator(0.0, 0.0, 0.0),
        )
        if created:
            nav_bounds = [created]
            unreal.log_warning(f"BR_APPLY_NAV_CREATED {created.get_name()}")

    for i, nb in enumerate(nav_bounds):
        nb.set_actor_location(unreal.Vector(0.0, 0.0, 250.0), False, False)
        nb.set_actor_scale3d(unreal.Vector(50.0, 50.0, 10.0))
        try:
            nb.set_actor_label(f"NAV_BOUNDS_{i + 1:02d}", mark_dirty=True)
        except Exception:
            pass
    unreal.log_warning(f"BR_APPLY_NAV_COUNT {len(nav_bounds)}")

    ws = world.get_world_settings()
    try:
        ws.set_editor_property("enable_world_bounds_checks", False)
    except Exception:
        pass


def tune_map_and_spawners():
    map_path, _ = load_first(CANDIDATE_MAPS)
    if not map_path:
        unreal.log_error("BR_APPLY_NO_MAP_FOUND")
        raise SystemExit(1)

    world = unreal.EditorLoadingAndSavingUtils.load_map(map_path)
    if not world:
        unreal.log_error(f"BR_APPLY_FAILED_LOAD_MAP {map_path}")
        raise SystemExit(1)

    actors = unreal.EditorLevelLibrary.get_all_level_actors()
    spawners = [a for a in actors if _is_bot_spawner(a)]
    unreal.log_warning(f"BR_APPLY_SPAWNER_COUNT {len(spawners)}")
    if len(spawners) == 0:
        unreal.log_warning(
            "BR_APPLY_RUNTIME_BOTS_MODE No editor spawner actors found; "
            "assuming bots are created by runtime blueprint logic."
        )

    for i, spawner in enumerate(spawners[: len(SPAWNER_POINTS)]):
        point = SPAWNER_POINTS[i]
        spawner.set_actor_location(point, False, False)
        try:
            spawner.set_actor_label(f"BOT_SPAWNER_{i + 1:02d}", mark_dirty=True)
        except Exception:
            pass
        try:
            spawner.set_folder_path("BOT_SYSTEM")
        except Exception:
            pass
        unreal.log_warning(
            f"BR_APPLY_SPAWNER_SET {spawner.get_name()} -> ({point.x},{point.y},{point.z})"
        )

    ensure_nav_bounds(world)
    saved = unreal.EditorAssetLibrary.save_asset(map_path, False)
    unreal.log_warning(f"BR_APPLY_MAP_SAVE {saved} PATH={map_path}")
    return map_path


def main():
    gm_path = tune_game_mode()
    map_path = tune_map_and_spawners()
    unreal.log_warning(f"BR_APPLY_COMPLETE GM={gm_path} MAP={map_path}")


if __name__ == "__main__":
    main()
