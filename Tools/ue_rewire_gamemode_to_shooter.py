import unreal

GM_BP_PATH = '/Game/FirstPerson/Blueprints/BP_FirstPersonGameMode'
SHOOTER_CHAR_BP = '/Game/Variant_Shooter/Blueprints/BP_ShooterCharacter'
SHOOTER_PC_BP = '/Game/Variant_Shooter/Blueprints/BP_ShooterPlayerController'


def load_bp(path: str):
    bp = unreal.EditorAssetLibrary.load_asset(path)
    if not bp:
        unreal.log_error(f'FAILED_TO_LOAD_BP {path}')
        raise SystemExit(1)
    return bp


def bp_class(bp):
    cls = bp.generated_class()
    if not cls:
        unreal.log_error(f'NO_GENERATED_CLASS {bp.get_path_name()}')
        raise SystemExit(1)
    return cls


gm_bp = load_bp(GM_BP_PATH)
char_bp = load_bp(SHOOTER_CHAR_BP)
pc_bp = load_bp(SHOOTER_PC_BP)

gm_cls = bp_class(gm_bp)
char_cls = bp_class(char_bp)
pc_cls = bp_class(pc_bp)

gm_cdo = unreal.get_default_object(gm_cls)

# Core gameplay classes
try:
    gm_cdo.set_editor_property('default_pawn_class', char_cls)
    unreal.log_warning(f'SET default_pawn_class -> {char_cls.get_name()}')
except Exception as ex:
    unreal.log_error(f'FAILED_SET_default_pawn_class {ex}')
    raise

try:
    gm_cdo.set_editor_property('player_controller_class', pc_cls)
    unreal.log_warning(f'SET player_controller_class -> {pc_cls.get_name()}')
except Exception as ex:
    unreal.log_warning(f'FAILED_SET_player_controller_class {ex}')

# Optional extras if exposed
for prop_name in ('hud_class', 'game_state_class', 'player_state_class', 'spectator_class'):
    try:
        current = gm_cdo.get_editor_property(prop_name)
        unreal.log_warning(f'CURRENT {prop_name} = {current}')
    except Exception:
        pass

saved = unreal.EditorAssetLibrary.save_loaded_asset(gm_bp)
unreal.log_warning(f'SAVE_GM={saved}')
