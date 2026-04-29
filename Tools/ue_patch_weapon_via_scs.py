import unreal

CHAR_BP_PATH = '/Game/FirstPerson/Blueprints/BP_FirstPersonCharacter'
PISTOL_MESH_PATH = '/Game/Weapons/Pistol/Meshes/SKM_Pistol.SKM_Pistol'

bp = unreal.EditorAssetLibrary.load_asset(CHAR_BP_PATH)
if not bp:
    unreal.log_error('NO_BP')
    raise SystemExit(1)

pistol = unreal.EditorAssetLibrary.load_asset(PISTOL_MESH_PATH)
if not pistol:
    unreal.log_error('NO_PISTOL_MESH')
    raise SystemExit(1)

scs = bp.get_editor_property('simple_construction_script')
if not scs:
    unreal.log_error('NO_SCS')
    raise SystemExit(1)

nodes = scs.get_all_nodes()
unreal.log(f'SCS_NODES={len(nodes)}')

patched = False
for n in nodes:
    try:
        node_name = str(n.get_variable_name())
    except Exception:
        node_name = '<unknown>'
    comp = n.get_editor_property('component_template')
    if not comp:
        continue

    cls_name = comp.get_class().get_name()
    unreal.log(f'NODE {node_name} CLASS {cls_name}')

    if 'FirstPersonMesh' in node_name and 'SkeletalMeshComponent' in cls_name:
        try:
            comp.set_editor_property('skeletal_mesh', pistol)
        except Exception as ex:
            unreal.log_warning(f'Could not set skeletal_mesh on {node_name}: {ex}')
            continue
        try:
            comp.set_editor_property('hidden_in_game', False)
        except Exception:
            pass
        try:
            comp.set_editor_property('visible', True)
        except Exception:
            pass
        unreal.log(f'PATCHED {node_name} with {PISTOL_MESH_PATH}')
        patched = True

if not patched:
    unreal.log_warning('NO_TARGET_FIRSTPERSONMESH_FOUND')

unreal.EditorAssetLibrary.save_loaded_asset(bp)
unreal.log('SAVE_DONE')
