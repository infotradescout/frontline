import unreal

GM_BP_PATH = '/Game/FirstPerson/Blueprints/BP_FirstPersonGameMode'
STD_CHAR_BP = '/Game/Variant_Shooter_Std/Blueprints/BP_ShooterCharacter'
STD_PC_BP = '/Game/Variant_Shooter_Std/Blueprints/BP_ShooterPlayerController'


def load_bp(path: str):
    bp = unreal.EditorAssetLibrary.load_asset(path)
    if not bp:
        unreal.log_error(f'FAILED_TO_LOAD_BP {path}')
        raise SystemExit(1)
    cls = bp.generated_class()
    if not cls:
        unreal.log_error(f'NO_GENERATED_CLASS {path}')
        raise SystemExit(1)
    return bp, cls


gm_bp, gm_cls = load_bp(GM_BP_PATH)
_, char_cls = load_bp(STD_CHAR_BP)
_, pc_cls = load_bp(STD_PC_BP)

gm_cdo = unreal.get_default_object(gm_cls)

gm_cdo.set_editor_property('default_pawn_class', char_cls)
unreal.log_warning(f'SET default_pawn_class -> {char_cls.get_name()}')

try:
    gm_cdo.set_editor_property('player_controller_class', pc_cls)
    unreal.log_warning(f'SET player_controller_class -> {pc_cls.get_name()}')
except Exception as ex:
    unreal.log_warning(f'FAILED_SET_player_controller_class {ex}')

saved = unreal.EditorAssetLibrary.save_loaded_asset(gm_bp)
unreal.log_warning(f'SAVE_GM={saved}')
