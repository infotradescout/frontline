import unreal

BP_PATH = '/Game/FirstPerson/Blueprints/BP_FirstPersonCharacter'
MANNY_PATH = '/Game/Characters/Mannequins/Meshes/SKM_Manny_Simple.SKM_Manny_Simple'
PISTOL_SM_PATH = '/Game/Weapons/Pistol/Meshes/SM_Pistol.SM_Pistol'

bp = unreal.EditorAssetLibrary.load_asset(BP_PATH)
if not bp:
    unreal.log_error('NO_BP')
    raise SystemExit(1)

bp_cls = bp.generated_class()
cdo = unreal.get_default_object(bp_cls)

# 1) Revert camera-weird patch: set body mesh back to Manny
manny = unreal.EditorAssetLibrary.load_asset(MANNY_PATH)
if not manny:
    unreal.log_error('NO_MANNY')
    raise SystemExit(1)

patched_body = False
for comp in cdo.get_components_by_class(unreal.SkeletalMeshComponent):
    if comp.get_name() == 'CharacterMesh0':
        try:
            comp.set_editor_property('skeletal_mesh', manny)
            comp.set_editor_property('owner_no_see', True)
            patched_body = True
            unreal.log_warning('PATCHED_BODY_MESH=CharacterMesh0->SKM_Manny_Simple owner_no_see=True')
        except Exception as ex:
            unreal.log_error(f'PATCH_BODY_FAILED: {ex}')

if not patched_body:
    unreal.log_warning('NO_CHARACTERMESH0_FOUND')

# 2) Try to add a visible static weapon mesh component to blueprint (no manual editor work)
pistol_sm = unreal.EditorAssetLibrary.load_asset(PISTOL_SM_PATH)
if not pistol_sm:
    unreal.log_warning('NO_PISTOL_STATIC_MESH')

try:
    subsys = unreal.get_engine_subsystem(unreal.SubobjectDataSubsystem)
    data = subsys.k2_gather_subobject_data_for_blueprint(bp)
    unreal.log_warning(f'SUBOBJECT_COUNT={len(data)}')

    # Locate parent: prefer CharacterMesh0 then CapsuleComponent root
    parent_handle = None
    for h in data:
        try:
            o = unreal.SubobjectDataBlueprintFunctionLibrary.get_object(
                unreal.SubobjectDataBlueprintFunctionLibrary.get_data(h)
            )
            if not o:
                continue
            n = o.get_name()
            if n == 'CharacterMesh0':
                parent_handle = h
                break
            if parent_handle is None and n in ('CollisionCylinder', 'CapsuleComponent'):
                parent_handle = h
        except Exception:
            pass

    if parent_handle and pistol_sm:
        params = unreal.AddNewSubobjectParams(
            parent_handle=parent_handle,
            new_class=unreal.StaticMeshComponent,
            blueprint_context=bp
        )
        result = subsys.add_new_subobject(params=params)

        # Handle API return variants
        new_handle = None
        fail_reason = ''
        if isinstance(result, tuple) and len(result) >= 2:
            new_handle, fail_reason = result[0], str(result[1])
        else:
            new_handle = result

        if not new_handle:
            unreal.log_warning(f'ADD_COMPONENT_FAILED: {fail_reason}')
        else:
            sdata = unreal.SubobjectDataBlueprintFunctionLibrary.get_data(new_handle)
            obj = unreal.SubobjectDataBlueprintFunctionLibrary.get_object(sdata)
            if obj and isinstance(obj, unreal.StaticMeshComponent):
                obj.set_editor_property('static_mesh', pistol_sm)
                obj.set_editor_property('hidden_in_game', False)
                obj.set_editor_property('visible', True)
                obj.set_editor_property('cast_shadow', False)
                try:
                    obj.set_editor_property('relative_location', unreal.Vector(60.0, 12.0, -8.0))
                    obj.set_editor_property('relative_rotation', unreal.Rotator(0.0, 0.0, 0.0))
                    obj.set_editor_property('relative_scale3d', unreal.Vector(1.0, 1.0, 1.0))
                except Exception:
                    pass
                unreal.log_warning('ADDED_WEAPON_COMPONENT=StaticMeshComponent(SM_Pistol)')
            else:
                unreal.log_warning('NEW_COMPONENT_OBJECT_NOT_STATICMESHCOMPONENT')
    else:
        unreal.log_warning('NO_PARENT_HANDLE_OR_NO_PISTOL')
except Exception as ex:
    unreal.log_warning(f'WEAPON_COMPONENT_PATH_FAILED: {ex}')

unreal.EditorAssetLibrary.save_loaded_asset(bp)
unreal.log_warning('SAVE_DONE')
