import unreal

MAP_PATH = '/Game/Variant_Shooter/Lvl_ArenaShooter'

unreal.log_warning(f'LOADING_MAP {MAP_PATH}')
world = unreal.EditorLoadingAndSavingUtils.load_map(MAP_PATH)
if not world:
    unreal.log_error('FAILED_TO_LOAD_MAP')
    raise SystemExit(1)

actors = unreal.EditorLevelLibrary.get_all_level_actors()
unreal.log_warning(f'ACTOR_COUNT {len(actors)}')

spawners = []
for a in actors:
    cls_name = a.get_class().get_name()
    if 'ShooterNPCSpawner' in cls_name:
        spawners.append(a)

unreal.log_warning(f'SPAWNER_COUNT {len(spawners)}')

keywords = ('respawn', 'spawn', 'cooldown', 'delay', 'count', 'max', 'min', 'wave', 'bot', 'kill', 'score', 'time', 'match', 'win', 'lose', 'end')

for idx, sp in enumerate(spawners):
    unreal.log_warning(f'SPAWNER_{idx} NAME={sp.get_name()} CLASS={sp.get_class().get_name()}')
    names = [n for n in dir(sp) if not n.startswith('_')]
    likely = [n for n in names if any(k in n.lower() for k in keywords)]
    likely = sorted(set(likely))
    unreal.log_warning(f'SPAWNER_{idx}_LIKELY_PROPS ' + ', '.join(likely[:200]))
    for n in likely[:80]:
        try:
            v = sp.get_editor_property(n)
            unreal.log_warning(f'SPAWNER_{idx}_VAL {n}={v}')
        except Exception:
            pass

gm_asset = unreal.EditorAssetLibrary.load_asset('/Game/Variant_Shooter/Blueprints/BP_ShooterGameMode')
if gm_asset and gm_asset.generated_class():
    cdo = unreal.get_default_object(gm_asset.generated_class())
    names = [n for n in dir(cdo) if not n.startswith('_')]
    likely = [n for n in names if any(k in n.lower() for k in keywords)]
    likely = sorted(set(likely))
    unreal.log_warning('GM_LIKELY_PROPS ' + ', '.join(likely[:200]))
    for n in likely[:120]:
        try:
            v = cdo.get_editor_property(n)
            unreal.log_warning(f'GM_VAL {n}={v}')
        except Exception:
            pass
else:
    unreal.log_warning('GM_MISSING_OR_NO_CLASS')
