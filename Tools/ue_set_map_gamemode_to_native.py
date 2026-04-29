import unreal

MAP_CANDIDATES = [
    "/Game/FirstPerson/Lvl_FirstPerson",
    "/Game/FirstPerson/FirstPerson/Lvl_FirstPerson",
]
NATIVE_GAMEMODE_CLASS = "/Script/FrontlineWarfare.FrontlineBRGameMode"


def _first_existing_asset(paths):
    for path in paths:
        if unreal.EditorAssetLibrary.does_asset_exist(path):
            return path
    return None


def main():
    target_map = _first_existing_asset(MAP_CANDIDATES)
    if not target_map:
        unreal.log_error("SET_GM_NATIVE_FAIL no candidate map found")
        raise SystemExit(1)

    gm_cls = unreal.load_class(None, NATIVE_GAMEMODE_CLASS)
    if not gm_cls:
        unreal.log_error(f"SET_GM_NATIVE_FAIL could not load class {NATIVE_GAMEMODE_CLASS}")
        raise SystemExit(1)

    unreal.EditorLevelLibrary.load_level(target_map)
    world = unreal.EditorLevelLibrary.get_editor_world()
    if not world:
        unreal.log_error("SET_GM_NATIVE_FAIL no editor world")
        raise SystemExit(1)

    world_settings = world.get_world_settings()
    world_settings.set_editor_property("default_game_mode", gm_cls)

    saved = unreal.EditorLevelLibrary.save_current_level()
    unreal.EditorLoadingAndSavingUtils.save_dirty_packages(True, True)

    unreal.log_warning(f"SET_GM_NATIVE_MAP {target_map}")
    unreal.log_warning(f"SET_GM_NATIVE_CLASS {NATIVE_GAMEMODE_CLASS}")
    unreal.log_warning(f"SET_GM_NATIVE_SAVED {saved}")


if __name__ == "__main__":
    main()
