import unreal

MAP_PATH = '/Game/Variant_Shooter/Lvl_ArenaShooter'

world = unreal.EditorLoadingAndSavingUtils.load_map(MAP_PATH)
if not world:
    unreal.log_error(f'FAILED_TO_LOAD_MAP {MAP_PATH}')
    raise SystemExit(1)

actors = unreal.EditorLevelLibrary.get_all_level_actors()
spawners = [a for a in actors if 'ShooterNPCSpawner' in a.get_class().get_name()]

unreal.log_warning(f'SPAWNER_FOUND_COUNT={len(spawners)}')

for i, actor in enumerate(spawners, start=1):
    label = f'BOT_SPAWNER_{i:02d}'

    try:
        actor.set_actor_label(label, mark_dirty=True)
    except Exception as ex:
        unreal.log_warning(f'LABEL_FAIL {actor.get_name()} {ex}')

    try:
        actor.set_folder_path('BOT_SYSTEM')
    except Exception as ex:
        unreal.log_warning(f'FOLDER_FAIL {actor.get_name()} {ex}')

    try:
        actor.set_is_temporarily_hidden_in_editor(False)
    except Exception:
        pass

    try:
        actor.set_is_temporarily_hidden_in_game(False)
    except Exception:
        pass

    try:
        actor.set_actor_enable_collision(True)
    except Exception:
        pass

    unreal.log_warning(f'SPAWNER_LABELED {actor.get_name()} -> {label}')

saved_level = False
try:
    saved_level = unreal.EditorLevelLibrary.save_current_level()
except Exception:
    saved_level = False

saved_packages = False
try:
    saved_packages = unreal.EditorLoadingAndSavingUtils.save_dirty_packages(True, True)
except Exception:
    saved_packages = False

unreal.log_warning(f'SAVE_LEVEL_RESULT={saved_level}')
unreal.log_warning(f'SAVE_PACKAGES_RESULT={saved_packages}')
