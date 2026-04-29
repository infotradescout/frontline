import unreal

CHAR_BP_PATH = '/Game/FirstPerson/Blueprints/BP_FirstPersonCharacter'
PC_BP_PATH = '/Game/FirstPerson/Blueprints/BP_FirstPersonPlayerController'
NEW_GM_PACKAGE_PATH = '/Game/FirstPerson/Blueprints'
NEW_GM_NAME = 'BP_FP_CleanGameMode'


def load_bp(path: str, required: bool = True):
    bp = unreal.EditorAssetLibrary.load_asset(path)
    if not bp and required:
        unreal.log_error(f'FAILED_TO_LOAD_BP {path}')
        raise SystemExit(1)
    return bp


def get_class_or_none(bp, label: str):
    if not bp:
        return None
    cls = bp.generated_class()
    unreal.log_warning(f'CLASS_CHECK {label} -> {cls}')
    return cls


def ensure_game_mode_blueprint():
    existing = unreal.EditorAssetLibrary.load_asset(f"{NEW_GM_PACKAGE_PATH}/{NEW_GM_NAME}")
    if existing:
        unreal.log_warning('USING_EXISTING_CLEAN_GAMEMODE')
        return existing

    factory = unreal.BlueprintFactory()
    factory.set_editor_property('parent_class', unreal.GameModeBase)
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    bp = asset_tools.create_asset(NEW_GM_NAME, NEW_GM_PACKAGE_PATH, unreal.Blueprint, factory)
    if not bp:
        unreal.log_error('FAILED_TO_CREATE_CLEAN_GAMEMODE')
        raise SystemExit(1)
    unreal.log_warning('CREATED_CLEAN_GAMEMODE')
    return bp


char_bp = load_bp(CHAR_BP_PATH)
pc_bp = load_bp(PC_BP_PATH, required=False)
char_cls = get_class_or_none(char_bp, 'CHAR')
pc_cls = get_class_or_none(pc_bp, 'PC')

if not char_cls:
    unreal.log_error('NO_CHAR_CLASS')
    raise SystemExit(1)

clean_gm_bp = ensure_game_mode_blueprint()
clean_gm_cls = clean_gm_bp.generated_class()
if not clean_gm_cls:
    unreal.log_error('NO_CLEAN_GM_CLASS')
    raise SystemExit(1)

clean_gm_cdo = unreal.get_default_object(clean_gm_cls)
clean_gm_cdo.set_editor_property('default_pawn_class', char_cls)
unreal.log_warning(f'SET_CLEAN_GM_default_pawn_class -> {char_cls.get_name()}')

if pc_cls:
    try:
        clean_gm_cdo.set_editor_property('player_controller_class', pc_cls)
        unreal.log_warning(f'SET_CLEAN_GM_player_controller_class -> {pc_cls.get_name()}')
    except Exception as ex:
        unreal.log_warning(f'FAILED_SET_CLEAN_GM_PC {ex}')

saved = unreal.EditorAssetLibrary.save_loaded_asset(clean_gm_bp)
unreal.log_warning(f'SAVE_CLEAN_GM={saved}')
