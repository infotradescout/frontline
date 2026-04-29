import unreal

GM_BP_PATH = '/Game/FirstPerson/Blueprints/BP_FirstPersonGameMode'
FP_CHAR_BP = '/Game/FirstPerson/Blueprints/BP_FirstPersonCharacter'
FP_PC_BP = '/Game/FirstPerson/Blueprints/BP_FirstPersonPlayerController'


def load_bp(path: str, required: bool = True):
    bp = unreal.EditorAssetLibrary.load_asset(path)
    if not bp and required:
        unreal.log_error(f'FAILED_TO_LOAD_BP {path}')
        raise SystemExit(1)
    return bp


def generated_class(bp, path: str):
    if not bp:
        return None
    cls = bp.generated_class()
    if not cls:
        unreal.log_error(f'NO_GENERATED_CLASS {path}')
        raise SystemExit(1)
    return cls


gm_bp = load_bp(GM_BP_PATH)
fp_char_bp = load_bp(FP_CHAR_BP)
fp_pc_bp = load_bp(FP_PC_BP, required=False)

gm_cls = generated_class(gm_bp, GM_BP_PATH)
fp_char_cls = generated_class(fp_char_bp, FP_CHAR_BP)
fp_pc_cls = generated_class(fp_pc_bp, FP_PC_BP) if fp_pc_bp else None

gm_cdo = unreal.get_default_object(gm_cls)

gm_cdo.set_editor_property('default_pawn_class', fp_char_cls)
unreal.log_warning(f'SET default_pawn_class -> {fp_char_cls.get_name()}')

if fp_pc_cls:
    try:
        gm_cdo.set_editor_property('player_controller_class', fp_pc_cls)
        unreal.log_warning(f'SET player_controller_class -> {fp_pc_cls.get_name()}')
    except Exception as ex:
        unreal.log_warning(f'FAILED_SET_player_controller_class {ex}')
else:
    unreal.log_warning('NO_FP_PLAYER_CONTROLLER_BP_USING_ENGINE_DEFAULT')

saved = unreal.EditorAssetLibrary.save_loaded_asset(gm_bp)
unreal.log_warning(f'SAVE_GM={saved}')
