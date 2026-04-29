import unreal

MAPS = [
    "/Game/FirstPerson/Lvl_FirstPerson",
    "/Game/FirstPerson/FirstPerson/Lvl_FirstPerson",
]


def summarize_map(map_path: str):
    if not unreal.EditorAssetLibrary.does_asset_exist(map_path):
        unreal.log_warning(f"MAP_COMPARE_MISSING {map_path}")
        return

    world = unreal.EditorLoadingAndSavingUtils.load_map(map_path)
    if not world:
        unreal.log_warning(f"MAP_COMPARE_LOAD_FAIL {map_path}")
        return

    actors = unreal.EditorLevelLibrary.get_all_level_actors()
    unreal.log_warning(f"MAP_COMPARE_TOTAL {map_path} {len(actors)}")

    sphere_like = 0
    yellow_block_like = 0
    spawners = 0

    for actor in actors:
        name = actor.get_name().lower()
        cls = actor.get_class().get_name().lower()
        if "spawn" in name or "spawner" in cls:
            spawners += 1
        if "sphere" in name or "ball" in name:
            sphere_like += 1

        if isinstance(actor, unreal.StaticMeshActor):
            smc = actor.get_component_by_class(unreal.StaticMeshComponent)
            if smc:
                mesh = smc.get_editor_property("static_mesh")
                if mesh:
                    mesh_name = mesh.get_name().lower()
                    if "cube" in mesh_name or "shape" in mesh_name or "floor" in mesh_name:
                        yellow_block_like += 1

    unreal.log_warning(f"MAP_COMPARE_SPHERE_LIKE {map_path} {sphere_like}")
    unreal.log_warning(f"MAP_COMPARE_BLOCK_LIKE {map_path} {yellow_block_like}")
    unreal.log_warning(f"MAP_COMPARE_SPAWNER_LIKE {map_path} {spawners}")


def main():
    for m in MAPS:
        summarize_map(m)


if __name__ == "__main__":
    main()
