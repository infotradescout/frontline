import unreal

bp = unreal.EditorAssetLibrary.load_asset('/Game/FirstPerson/Blueprints/BP_FirstPersonCharacter')
if not bp:
    unreal.log_error('NO_BP')
    raise SystemExit(1)
cls = bp.generated_class()
cdo = unreal.get_default_object(cls)

skeletal_components = cdo.get_components_by_class(unreal.SkeletalMeshComponent)
unreal.log_warning(f'SK_COUNT={len(skeletal_components)}')

for comp in skeletal_components:
    mesh = None
    try:
        mesh = comp.get_editor_property('skeletal_mesh')
    except Exception:
        pass
    unreal.log_warning(f'SK_COMP {comp.get_name()} -> {mesh}')
