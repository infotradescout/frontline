import unreal

BP_PATH = '/Game/FirstPerson/Blueprints/BP_FirstPersonCharacter.BP_FirstPersonCharacter'
WEAPON_COMPONENT_NAME = 'WeaponMesh'


def log(msg):
    unreal.log('[frontline-fix] ' + str(msg))


def warn(msg):
    unreal.log_warning('[frontline-fix] ' + str(msg))


def err(msg):
    unreal.log_error('[frontline-fix] ' + str(msg))


def find_node_by_name(nodes, name):
    for n in nodes:
        try:
            if str(n.get_variable_name()) == name:
                return n
        except Exception:
            pass
    return None


def main():
    bp = unreal.load_asset(BP_PATH)
    if not bp:
        err(f'Could not load blueprint: {BP_PATH}')
        return

    scs = bp.get_editor_property('simple_construction_script')
    if not scs:
        err('Blueprint has no SimpleConstructionScript')
        return

    nodes = list(scs.get_all_nodes())

    camera_node = find_node_by_name(nodes, 'FirstPersonCamera')
    if not camera_node:
        err('FirstPersonCamera component not found in BP_FirstPersonCharacter')
        return

    weapon_node = find_node_by_name(nodes, WEAPON_COMPONENT_NAME)

    if not weapon_node:
        log('WeaponMesh not found, creating StaticMeshComponent node')
        weapon_node = scs.create_node(unreal.StaticMeshComponent, WEAPON_COMPONENT_NAME)
        # Attach to camera then add to SCS root so it persists
        weapon_node.set_parent(camera_node)
        scs.add_node(weapon_node)

    # Ensure parent is camera
    try:
        weapon_node.set_parent(camera_node)
    except Exception as ex:
        warn(f'Could not set parent to camera: {ex}')

    comp = weapon_node.get_editor_property('component_template')
    if not comp:
        err('WeaponMesh component template not found')
        return

    cube = unreal.load_asset('/Engine/BasicShapes/Cube.Cube')
    if not cube:
        cube = unreal.load_asset('/Game/LevelPrototyping/Meshes/SM_Cube.SM_Cube')

    if cube:
        comp.set_editor_property('static_mesh', cube)
    else:
        warn('Could not load cube mesh; leaving existing static mesh')

    comp.set_editor_property('visible', True)
    comp.set_editor_property('hidden_in_game', False)

    # Force obvious position in front of first-person camera
    comp.set_editor_property('relative_location', unreal.Vector(60.0, 0.0, 0.0))
    comp.set_editor_property('relative_rotation', unreal.Rotator(0.0, 0.0, 0.0))
    comp.set_editor_property('relative_scale3d', unreal.Vector(0.5, 0.2, 0.2))

    # Try mobility when available
    try:
        comp.set_editor_property('mobility', unreal.ComponentMobility.MOVABLE)
    except Exception:
        pass

    unreal.EditorAssetLibrary.save_loaded_asset(bp)
    unreal.EditorAssetLibrary.save_asset('/Game/FirstPerson/Blueprints/BP_FirstPersonCharacter', only_if_is_dirty=False)

    # Compile BP to apply changes
    try:
        unreal.KismetEditorUtilities.compile_blueprint(bp)
    except Exception as ex:
        warn(f'Compile failed (manual compile may be needed): {ex}')

    log('Done. BP_FirstPersonCharacter updated. Press Play to verify visible weapon cube.')


if __name__ == '__main__':
    main()
