import unreal

bp = unreal.EditorAssetLibrary.load_asset('/Game/FirstPerson/Blueprints/BP_FirstPersonCharacter')
if not bp:
    unreal.log_error('NO_BP')
    raise SystemExit(1)

cls = bp.generated_class()
cdo = unreal.get_default_object(cls)

all_components = cdo.get_components_by_class(unreal.ActorComponent)
unreal.log_warning(f'COMP_COUNT={len(all_components)}')

for comp in all_components:
    cname = comp.get_name()
    cls_name = comp.get_class().get_name()
    line = f'COMP {cname} CLASS {cls_name}'

    if isinstance(comp, unreal.SkeletalMeshComponent):
        try:
            mesh = comp.get_editor_property('skeletal_mesh')
        except Exception:
            mesh = None
        line += f' SKELETAL_MESH={mesh}'
    elif isinstance(comp, unreal.StaticMeshComponent):
        try:
            mesh = comp.get_editor_property('static_mesh')
        except Exception:
            mesh = None
        line += f' STATIC_MESH={mesh}'

    if isinstance(comp, unreal.SceneComponent):
        try:
            parent = comp.get_attach_parent()
            parent_name = parent.get_name() if parent else 'None'
        except Exception:
            parent_name = 'Unknown'
        line += f' PARENT={parent_name}'

    unreal.log_warning(line)
