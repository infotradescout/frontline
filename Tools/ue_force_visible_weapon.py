import unreal

CHAR_BP_PATH = '/Game/FirstPerson/Blueprints/BP_FirstPersonCharacter'
PISTOL_MESH_PATH = '/Game/Weapons/Pistol/Meshes/SKM_Pistol.SKM_Pistol'

bp_asset = unreal.EditorAssetLibrary.load_asset(CHAR_BP_PATH)
if not bp_asset:
    unreal.log_error(f'Could not load {CHAR_BP_PATH}')
    raise SystemExit(1)

bp_class = bp_asset.generated_class()
if not bp_class:
    unreal.log_error('No generated class on BP asset')
    raise SystemExit(1)

cdo = unreal.get_default_object(bp_class)
if not cdo:
    unreal.log_error('No CDO')
    raise SystemExit(1)

pistol = unreal.EditorAssetLibrary.load_asset(PISTOL_MESH_PATH)
if not pistol:
    unreal.log_error(f'Could not load pistol mesh: {PISTOL_MESH_PATH}')
    raise SystemExit(1)

skeletal_components = cdo.get_components_by_class(unreal.SkeletalMeshComponent)
unreal.log(f'Found {len(skeletal_components)} skeletal mesh components on CDO')

target = None
for comp in skeletal_components:
    n = comp.get_name().lower()
    unreal.log(f'Component: {comp.get_name()}')
    if 'firstperson' in n or 'first_person' in n:
        target = comp

if target is None and skeletal_components:
    target = skeletal_components[0]

if target is None:
    unreal.log_error('No skeletal mesh component found to apply weapon fallback')
    raise SystemExit(1)

# Force a visible weapon mesh as emergency fallback.
try:
    target.set_editor_property('skeletal_mesh', pistol)
except Exception as ex:
    unreal.log_error(f'Failed to set skeletal_mesh on {target.get_name()}: {ex}')
    raise

try:
    target.set_editor_property('hidden_in_game', False)
except Exception:
    pass

try:
    target.set_editor_property('visible', True)
except Exception:
    pass

unreal.EditorAssetLibrary.save_loaded_asset(bp_asset)
unreal.log(f'Applied fallback weapon mesh to component: {target.get_name()}')
