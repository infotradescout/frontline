import unreal

MAP_PATH = "/Game/FirstPerson/Lvl_FirstPerson"
TEMPLATE_MATERIAL_PATH = "/Game/FirstPerson/MI_FirstPersonColorway"


def _matches_template_material(actor: unreal.Actor) -> bool:
    if not isinstance(actor, unreal.StaticMeshActor):
        return False

    smc = actor.get_component_by_class(unreal.StaticMeshComponent)
    if not smc:
        return False

    for mat in smc.get_materials():
        if not mat:
            continue
        if mat.get_path_name().startswith(TEMPLATE_MATERIAL_PATH):
            return True
    return False


def main():
    world = unreal.EditorLoadingAndSavingUtils.load_map(MAP_PATH)
    if not world:
        unreal.log_error(f"CLEANUP_FAILED_LOAD_MAP {MAP_PATH}")
        raise SystemExit(1)

    actors = unreal.EditorLevelLibrary.get_all_level_actors()
    removed = 0

    for actor in actors:
        if _matches_template_material(actor):
            unreal.log_warning(f"CLEANUP_REMOVE {actor.get_name()}")
            if unreal.EditorLevelLibrary.destroy_actor(actor):
                removed += 1

    saved = unreal.EditorLevelLibrary.save_current_level()
    unreal.log_warning(f"CLEANUP_REMOVED_TOTAL {removed}")
    unreal.log_warning(f"CLEANUP_SAVE_RESULT {saved}")


if __name__ == "__main__":
    main()
