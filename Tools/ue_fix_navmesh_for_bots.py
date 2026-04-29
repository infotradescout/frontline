import unreal

MAP_CANDIDATES = [
    '/Game/FirstPerson/Lvl_FirstPerson',
    '/Game/FirstPerson/FirstPerson/Lvl_FirstPerson',
    '/Game/Variant_Shooter/Lvl_ArenaShooter',
    '/Game/Variant_Shooter_BP/Lvl_Shooter',
    '/Game/Variant_Shooter_Std/Lvl_Shooter',
]


def _load_first_map(paths):
    for path in paths:
        if unreal.EditorAssetLibrary.does_asset_exist(path):
            world = unreal.EditorLoadingAndSavingUtils.load_map(path)
            if world:
                unreal.log_warning(f'NAV_FIX_MAP {path}')
                return path, world
    return None, None


GROUND_SPAWN_POINTS = [
    unreal.Vector(-900.0, -900.0, 40.0),
    unreal.Vector(900.0, -900.0, 40.0),
    unreal.Vector(-900.0, 900.0, 40.0),
    unreal.Vector(900.0, 900.0, 40.0),
    unreal.Vector(0.0, -900.0, 40.0),
    unreal.Vector(0.0, 900.0, 40.0),
    unreal.Vector(-900.0, 0.0, 40.0),
    unreal.Vector(900.0, 0.0, 40.0),
]


def _is_spawn_actor(actor):
    cls = actor.get_class().get_name().lower()
    name = actor.get_name().lower()
    if 'playerstart' in cls:
        return True
    if 'targetpoint' in cls:
        return True
    if 'spawn' in cls or 'spawn' in name:
        return True
    return False

map_path, world = _load_first_map(MAP_CANDIDATES)
if not world:
    unreal.log_error('FAILED_TO_LOAD_MAP_CANDIDATES')
    raise SystemExit(1)

actors = unreal.EditorLevelLibrary.get_all_level_actors()
nav_bounds = [a for a in actors if a.get_class().get_name() == 'NavMeshBoundsVolume']
recast = [a for a in actors if 'RecastNavMesh' in a.get_class().get_name()]
unreal.log_warning(f'NAV_BOUNDS_COUNT={len(nav_bounds)} RECAST_COUNT={len(recast)}')

spawn_actors = [a for a in actors if _is_spawn_actor(a)]
unreal.log_warning(f'SPAWN_ACTOR_COUNT={len(spawn_actors)}')
for i, actor in enumerate(spawn_actors):
    point = GROUND_SPAWN_POINTS[i % len(GROUND_SPAWN_POINTS)]
    try:
        actor.modify()
    except Exception:
        pass
    actor.set_actor_location(point, False, False)
    try:
        actor.set_actor_label(f'GROUND_SPAWN_{i+1:02d}', mark_dirty=True)
    except Exception:
        pass
    unreal.log_warning(f'SPAWN_ACTOR_SET {actor.get_name()} -> ({point.x},{point.y},{point.z})')

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
    nb.set_actor_location(unreal.Vector(0.0, 0.0, 320.0), False, False)
    # Expand bounds to cover upper platforms and lower arena lanes.
    nb.set_actor_scale3d(unreal.Vector(90.0, 90.0, 80.0))
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

try:
    unreal.SystemLibrary.execute_console_command(world, 'RebuildNavigation')
    unreal.log_warning('NAV_PATH_BUILD_TRIGGERED')
except Exception as ex:
    unreal.log_warning(f'NAV_PATH_BUILD_SKIP {ex}')

# Save map asset.
saved = False
dirty_saved = False
try:
    dirty_saved = unreal.EditorLoadingAndSavingUtils.save_dirty_packages(True, True)
except Exception as ex:
    unreal.log_warning(f'SAVE_DIRTY_PACKAGES_SKIP {ex}')

try:
    saved = unreal.EditorAssetLibrary.save_asset(map_path, False)
except Exception as ex:
    unreal.log_warning(f'SAVE_MAP_EXCEPTION {ex}')

unreal.log_warning(f'SAVE_DIRTY_PACKAGES_RESULT={dirty_saved}')
unreal.log_warning(f'SAVE_MAP_RESULT={saved}')
