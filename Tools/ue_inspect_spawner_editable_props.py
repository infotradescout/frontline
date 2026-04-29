import unreal

MAP_PATH = '/Game/Variant_Shooter/Lvl_ArenaShooter'

world = unreal.EditorLoadingAndSavingUtils.load_map(MAP_PATH)
if not world:
    unreal.log_error(f'FAILED_TO_LOAD_MAP {MAP_PATH}')
    raise SystemExit(1)

actors = unreal.EditorLevelLibrary.get_all_level_actors()
spawners = [a for a in actors if 'ShooterNPCSpawner' in a.get_class().get_name()]

unreal.log_warning(f'SPAWNER_COUNT={len(spawners)}')

for idx, a in enumerate(spawners):
    loc = a.get_actor_location()
    unreal.log_warning(f'SPAWNER_{idx}_NAME={a.get_name()} LOC=({loc.x:.1f},{loc.y:.1f},{loc.z:.1f})')

    readable = []
    for name in dir(a):
        if name.startswith('_'):
            continue
        try:
            value = a.get_editor_property(name)
            readable.append((name, value))
        except Exception:
            continue

    unreal.log_warning(f'SPAWNER_{idx}_READABLE_PROP_COUNT={len(readable)}')

    # Emit likely gameplay knobs first
    keys = ('spawn', 'respawn', 'npc', 'bot', 'delay', 'time', 'rate', 'count', 'max', 'min', 'radius')
    likely = [(n, v) for (n, v) in readable if any(k in n.lower() for k in keys)]
    for n, v in likely:
        unreal.log_warning(f'SPAWNER_{idx}_LIKELY {n}={v}')

    # Emit all readable names for fallback parsing
    for n, v in readable:
        unreal.log_warning(f'SPAWNER_{idx}_PROP {n}={v}')
