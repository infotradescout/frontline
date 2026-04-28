import unreal

BP_PATH = '/Game/FirstPerson/Blueprints/BP_FirstPersonCharacter'

bp = unreal.EditorAssetLibrary.load_asset(BP_PATH)
if not bp:
    unreal.log_error(f'FAILED_TO_LOAD {BP_PATH}')
    raise SystemExit(1)

unreal.log_warning(f'BP_LOADED {BP_PATH}')

# Inspect construction script nodes (blueprint-added components)
try:
    scs = bp.get_editor_property('SimpleConstructionScript')
    if scs:
        nodes = scs.get_all_nodes()
        unreal.log_warning(f'SCS_NODE_COUNT {len(nodes)}')
        for n in nodes:
            comp_tmpl = n.get_editor_property('component_template')
            comp_class = comp_tmpl.get_class().get_name() if comp_tmpl else 'None'
            comp_name = comp_tmpl.get_name() if comp_tmpl else 'None'
            var_name = str(n.get_variable_name())
            unreal.log_warning(f'SCS_NODE VAR={var_name} COMP_CLASS={comp_class} COMP_NAME={comp_name}')
    else:
        unreal.log_warning('NO_SCS')
except Exception as ex:
    unreal.log_error(f'SCS_INSPECT_ERROR {ex}')

# Inspect class default properties that may influence weapons
try:
    gen = bp.generated_class()
    cdo = unreal.get_default_object(gen) if gen else None
    if cdo:
        prop_names = [
            'default_mapping_context',
            'fire_action',
            'jump_action',
            'look_action',
            'move_action',
            'weapon_component',
            'weapon_class',
            'projectile_class',
        ]
        for p in prop_names:
            try:
                v = cdo.get_editor_property(p)
                unreal.log_warning(f'CDO_PROP {p}={v}')
            except Exception:
                pass
except Exception as ex:
    unreal.log_error(f'CDO_INSPECT_ERROR {ex}')
