import unreal

bp = unreal.EditorAssetLibrary.load_asset('/Game/FirstPerson/Blueprints/BP_FirstPersonCharacter')
if not bp:
    unreal.log_error('NO_BP')
    raise SystemExit(1)

cls = bp.generated_class()
cdo = unreal.get_default_object(cls)

unreal.log_warning(f'CDO_TYPE={type(cdo)}')

candidates = []
for name in dir(cdo):
    low = name.lower()
    if any(k in low for k in ['weapon', 'equip', 'fire', 'shoot', 'ammo', 'inventory', 'loadout', 'projectile', 'input', 'action']):
        candidates.append(name)

unreal.log_warning(f'CANDIDATE_ATTR_COUNT={len(candidates)}')
for name in sorted(candidates):
    try:
        val = getattr(cdo, name)
        unreal.log_warning(f'ATTR {name} TYPE={type(val)}')
    except Exception as ex:
        unreal.log_warning(f'ATTR {name} READ_FAIL={ex}')

# Probe likely editable properties by trying get_editor_property on common keys
common_props = [
    'default_weapon', 'default_weapon_class', 'weapon_class', 'equipped_weapon',
    'starting_weapon', 'initial_weapon', 'current_weapon', 'weapon_component',
    'input_mapping_context', 'default_mapping_context', 'fire_action',
    'shoot_action', 'aim_action', 'jump_action', 'move_action', 'look_action'
]
for p in common_props:
    try:
        v = cdo.get_editor_property(p)
        unreal.log_warning(f'PROP {p} = {v}')
    except Exception:
        pass
