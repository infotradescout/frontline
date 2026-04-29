import unreal

MAP_PATH = '/Game/Variant_Shooter/Lvl_ArenaShooter'
TARGET_POINTS = [
    unreal.Vector(-950.0, -950.0, 120.0),
    unreal.Vector( 950.0, -950.0, 120.0),
    unreal.Vector(-950.0,  950.0, 120.0),
    unreal.Vector( 950.0,  950.0, 120.0),
]

world = unreal.EditorLoadingAndSavingUtils.load_map(MAP_PATH)
if not world:
    unreal.log_error(f'FAILED_TO_LOAD_MAP {MAP_PATH}')
    raise SystemExit(1)

actors = unreal.EditorLevelLibrary.get_all_level_actors()
spawners = [a for a in actors if 'ShooterNPCSpawner' in a.get_class().get_name()]
unreal.log_warning(f'LAYOUT_EXISTING_SPAWNERS={len(spawners)}')

if len(spawners) == 0:
    unreal.log_error('NO_EXISTING_SPAWNERS')
    raise SystemExit(1)

spawner_class = spawners[0].get_class()

# Ensure at least 4 spawners for better coverage
while len(spawners) < 4:
    new_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(spawner_class, TARGET_POINTS[len(spawners)], unreal.Rotator(0.0, 0.0, 0.0))
    if new_actor:
        spawners.append(new_actor)
        unreal.log_warning(f'SPAWNER_ADDED {new_actor.get_name()}')
    else:
        unreal.log_warning('SPAWNER_ADD_FAILED')
        break

# Reposition first 4 spawners to safe points
for i, point in enumerate(TARGET_POINTS):
    if i >= len(spawners):
        break
    sp = spawners[i]
    sp.set_actor_location(point, False, False)
    try:
        sp.set_actor_label(f'BOT_SPAWNER_{i+1:02d}', mark_dirty=True)
    except Exception:
        pass
    try:
        sp.set_folder_path('BOT_SYSTEM')
    except Exception:
        pass
    unreal.log_warning(f'SPAWNER_SET {sp.get_name()} -> ({point.x},{point.y},{point.z})')

saved = False
try:
    saved = unreal.EditorAssetLibrary.save_asset(MAP_PATH, False)
except Exception as ex:
    unreal.log_warning(f'SAVE_MAP_EXCEPTION {ex}')

unreal.log_warning(f'SAVE_MAP_RESULT={saved}')
