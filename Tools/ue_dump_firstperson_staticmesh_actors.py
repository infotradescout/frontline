import unreal

MAP_PATH = "/Game/FirstPerson/Lvl_FirstPerson"


def _asset_path(obj):
    if not obj:
        return "None"
    try:
        return obj.get_path_name()
    except Exception:
        return str(obj)


def main():
    world = unreal.EditorLoadingAndSavingUtils.load_map(MAP_PATH)
    if not world:
        unreal.log_error(f"DUMP_FAILED_LOAD_MAP {MAP_PATH}")
        raise SystemExit(1)

    actors = unreal.EditorLevelLibrary.get_all_level_actors()
    unreal.log_warning(f"DUMP_MAP {MAP_PATH}")
    unreal.log_warning(f"DUMP_ACTOR_TOTAL {len(actors)}")

    sm_count = 0
    for actor in actors:
        if not isinstance(actor, unreal.StaticMeshActor):
            continue
        sm_count += 1
        smc = actor.get_component_by_class(unreal.StaticMeshComponent)
        mesh_path = "None"
        mats = []
        if smc:
            mesh = smc.get_editor_property("static_mesh")
            mesh_path = _asset_path(mesh)
            for i, mat in enumerate(smc.get_materials()):
                mats.append(f"{i}:{_asset_path(mat)}")
        loc = actor.get_actor_location()
        unreal.log_warning(
            "DUMP_SM_ACTOR "
            f"NAME={actor.get_name()} "
            f"MESH={mesh_path} "
            f"LOC=({loc.x:.1f},{loc.y:.1f},{loc.z:.1f}) "
            f"MATS=[{'|'.join(mats)}]"
        )

    unreal.log_warning(f"DUMP_SM_TOTAL {sm_count}")


if __name__ == "__main__":
    main()
