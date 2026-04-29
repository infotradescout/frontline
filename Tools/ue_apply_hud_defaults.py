import unreal

GM_PATHS = [
    '/Game/Variant_Shooter/Blueprints/BP_ShooterGameMode',
    '/Game/Variant_Shooter_BP/Blueprints/BP_ShooterGameMode',
    '/Game/Variant_Shooter_Std/Blueprints/BP_ShooterGameMode',
    '/Game/FirstPerson/Blueprints/BP_FirstPersonGameMode',
    '/Game/FirstPerson/FirstPerson/Blueprints/BP_FirstPersonGameMode',
]

UI_PATHS = [
    '/Game/Variant_Shooter/UI/UI_Shooter',
    '/Game/Variant_Shooter_Std/UI/UI_Shooter',
]


def load(path: str):
    obj = unreal.EditorAssetLibrary.load_asset(path)
    unreal.log_warning(f'HUD_CHECK {path} EXISTS={obj is not None}')
    return obj


def load_first(paths: list[str]):
    for path in paths:
        obj = load(path)
        if obj is not None:
            return path, obj
    return None, None


gm_path, gm_bp = load_first(GM_PATHS)
ui_path, ui = load_first(UI_PATHS)
unreal.log_warning(f'HUD_CHECK ACTIVE_GM_PATH={gm_path}')
unreal.log_warning(f'HUD_CHECK ACTIVE_UI_PATH={ui_path}')

if not gm_bp:
    raise SystemExit(1)

# If UI_Shooter is a widget blueprint, it cannot be assigned to HUDClass directly.
# We still validate it exists so the shooter controller/game mode can use it at runtime.

gm_cls = gm_bp.generated_class()
if gm_cls:
    cdo = unreal.get_default_object(gm_cls)
    try:
        hud_class = cdo.get_editor_property('hud_class')
        unreal.log_warning(f'HUD_APPLY CURRENT_hud_class={hud_class}')
    except Exception as ex:
        unreal.log_warning(f'HUD_APPLY HUD_PROPERTY_READ_FAILED={ex}')

saved = unreal.EditorAssetLibrary.save_loaded_asset(gm_bp)
unreal.log_warning(f'HUD_APPLY SAVE_GM={saved}')
