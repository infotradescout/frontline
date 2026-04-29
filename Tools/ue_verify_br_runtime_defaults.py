import unreal

MAP_PATH = "/Game/FirstPerson/Lvl_FirstPerson"
CLASS_PATH = "/Script/FrontlineWarfare.FrontlineBRGameMode"


def main():
    cls = unreal.load_class(None, CLASS_PATH)
    if not cls:
        unreal.log_error(f"BR_DEFAULTS_VERIFY_FAIL class missing {CLASS_PATH}")
        raise SystemExit(1)

    cdo = unreal.get_default_object(cls)
    unreal.log_warning(f"BR_DEFAULTS_WarmupSeconds {cdo.get_editor_property('warmup_seconds')}")
    unreal.log_warning(f"BR_DEFAULTS_LiveMatchSeconds {cdo.get_editor_property('live_match_seconds')}")
    unreal.log_warning(f"BR_DEFAULTS_RestartDelaySeconds {cdo.get_editor_property('restart_delay_seconds')}")
    unreal.log_warning(f"BR_DEFAULTS_TargetBotCount {cdo.get_editor_property('target_bot_count')}")
    unreal.log_warning(f"BR_DEFAULTS_BotSpawnRadius {cdo.get_editor_property('bot_spawn_radius')}")
    unreal.log_warning(f"BR_DEFAULTS_AnnounceWinnerOnScreen {cdo.get_editor_property('announce_winner_on_screen')}")
    unreal.log_warning(f"BR_DEFAULTS_WinnerAnnouncementSeconds {cdo.get_editor_property('winner_announcement_seconds')}")

    unreal.EditorLevelLibrary.load_level(MAP_PATH)
    world = unreal.EditorLevelLibrary.get_editor_world()
    ws = world.get_world_settings() if world else None
    if ws:
        gm = ws.get_editor_property('default_game_mode')
        unreal.log_warning(f"BR_DEFAULTS_MapDefaultGameMode {gm.get_name() if gm else 'None'}")

    unreal.log_warning("BR_DEFAULTS_VERIFY_COMPLETE")


if __name__ == "__main__":
    main()
