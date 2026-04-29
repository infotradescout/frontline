import unreal

MAP_PATH = '/Game/Variant_Shooter/Lvl_ArenaShooter'

world = unreal.EditorLoadingAndSavingUtils.load_map(MAP_PATH)
if not world:
    unreal.log_error(f'FAILED_TO_LOAD_MAP {MAP_PATH}')
    raise SystemExit(1)

actors = unreal.EditorLevelLibrary.get_all_level_actors()
nav_bounds = [a for a in actors if a.get_class().get_name() == 'NavMeshBoundsVolume']
recast = [a for a in actors if 'RecastNavMesh' in a.get_class().get_name()]
unreal.log_warning(f'NAV_BOUNDS_COUNT={len(nav_bounds)} RECAST_COUNT={len(recast)}')

# Ensure at least one NavMeshBoundsVolume exists and covers arena.
if not nav_bounds:
    nb_class = unreal.NavMeshBoundsVolume
    nb = unreal.EditorLevelLibrary.spawn_actor_from_class(nb_class, unreal.Vector(0.0, 0.0, 200.0), unreal.Rotator(0.0, 0.0, 0.0))
    if not nb:
        unreal.log_error('FAILED_TO_CREATE_NAV_BOUNDS')
        raise SystemExit(1)
    nav_bounds = [nb]
    unreal.log_warning(f'CREATED_NAV_BOUNDS={nb.get_name()}')

for i, nb in enumerate(nav_bounds):
    nb.set_actor_location(unreal.Vector(0.0, 0.0, 250.0), False, False)
    nb.set_actor_scale3d(unreal.Vector(50.0, 50.0, 10.0))
    try:
        nb.set_actor_label(f'NAV_BOUNDS_{i+1:02d}', mark_dirty=True)
    except Exception:
        pass
    unreal.log_warning(f'NAV_BOUNDS_SET {nb.get_name()}')

# Ensure world nav settings are navigation-friendly.
ws = world.get_world_settings()
try:
    ws.set_editor_property('enable_world_bounds_checks', False)
except Exception:
    pass

# Save map asset.
saved = False
try:
    saved = unreal.EditorAssetLibrary.save_asset(MAP_PATH, False)
except Exception as ex:
    unreal.log_warning(f'SAVE_MAP_EXCEPTION {ex}')

unreal.log_warning(f'SAVE_MAP_RESULT={saved}')
