import unreal

GM_PATH = '/Game/Variant_Shooter/Blueprints/BP_ShooterGameMode'
UI_PATH = '/Game/Variant_Shooter/UI/UI_Shooter'


def load(path: str):
    obj = unreal.EditorAssetLibrary.load_asset(path)
    unreal.log_warning(f'HUD_CHECK {path} EXISTS={obj is not None}')
    return obj


gm_bp = load(GM_PATH)
ui = load(UI_PATH)

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
