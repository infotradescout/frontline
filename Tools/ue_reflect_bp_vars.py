import unreal

TARGETS = [
    '/Game/Variant_Shooter/Blueprints/AI/BP_ShooterNPCSpawner',
    '/Game/Variant_Shooter/Blueprints/BP_ShooterGameMode',
]

for p in TARGETS:
    bp = unreal.EditorAssetLibrary.load_asset(p)
    if not bp:
        unreal.log_warning(f'REFLECT_MISSING {p}')
        continue

    unreal.log_warning(f'REFLECT_TARGET {p}')

    # Try blueprint-side variable descriptors
    for attr in ('new_variables', 'NewVariables'):
        try:
            vars_arr = bp.get_editor_property(attr)
            unreal.log_warning(f'REFLECT_{attr}_COUNT {len(vars_arr)}')
            for v in vars_arr:
                try:
                    unreal.log_warning(f'BP_VAR {v.var_name} TYPE={v.var_type.pin_category}/{v.var_type.pin_sub_category_object}')
                except Exception:
                    unreal.log_warning(f'BP_VAR_RAW {v}')
        except Exception as ex:
            unreal.log_warning(f'REFLECT_{attr}_ERR {ex}')

    cls = bp.generated_class()
    if not cls:
        unreal.log_warning('REFLECT_NO_CLASS')
        continue

    unreal.log_warning(f'REFLECT_CLASS {cls.get_name()}')

    # Dump callable members with likely names
    names = [n for n in dir(cls) if not n.startswith('_')]
    keys = ('spawn', 'respawn', 'wave', 'match', 'end', 'score', 'kill', 'bot', 'time', 'round')
    likely = sorted(set([n for n in names if any(k in n.lower() for k in keys)]))
    unreal.log_warning('REFLECT_CLASS_LIKELY ' + ', '.join(likely[:300]))
