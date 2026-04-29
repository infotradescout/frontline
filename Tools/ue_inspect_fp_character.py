import unreal

ASSET_PATH = '/Game/FirstPerson/Blueprints/BP_FirstPersonCharacter'

asset = unreal.EditorAssetLibrary.load_asset(ASSET_PATH)
if not asset:
    unreal.log_error(f'FAILED load asset: {ASSET_PATH}')
    raise SystemExit(1)

# Try blueprint generated class CDO first
try:
    bp_cls = asset.generated_class()
except Exception:
    bp_cls = None

if not bp_cls:
    unreal.log_warning('No generated class on asset; listing generic editor properties only.')
    props = sorted([str(n) for n in asset.get_editor_property_names()])
    unreal.log('ASSET_EDITOR_PROPERTIES_START')
    for p in props:
        unreal.log(p)
    unreal.log('ASSET_EDITOR_PROPERTIES_END')
    raise SystemExit(0)

cdo = unreal.get_default_object(bp_cls)
prop_names = sorted([str(n) for n in cdo.get_editor_property_names()])

unreal.log('CDO_PROPERTIES_START')
for p in prop_names:
    if 'weapon' in p.lower() or 'equip' in p.lower() or 'gun' in p.lower() or 'inventory' in p.lower() or 'loadout' in p.lower():
        unreal.log(f'* {p}')
unreal.log('CDO_PROPERTIES_END')

# Dump candidate values for easier diagnosis
for p in prop_names:
    low = p.lower()
    if 'weapon' in low or 'equip' in low or 'gun' in low or 'inventory' in low or 'loadout' in low:
        try:
            v = cdo.get_editor_property(p)
            unreal.log(f'VALUE {p} = {v}')
        except Exception as ex:
            unreal.log_warning(f'VALUE_READ_FAILED {p}: {ex}')
