import unreal

GM_PATH = '/Game/Variant_Shooter/Blueprints/BP_ShooterGameMode'

TARGET_VALUES = {
    'goal_score': 25,
    'time_limit': 12,
    'num_bots': 10,
    'minimum_respawn_delay': 2.0,
    'inactive_player_state_life_span': 120.0,
    'max_inactive_players': 16,
}

bp = unreal.EditorAssetLibrary.load_asset(GM_PATH)
if not bp:
    unreal.log_error(f'TUNING_MISSING_GM {GM_PATH}')
    raise SystemExit(1)

cls = bp.generated_class()
if not cls:
    unreal.log_error('TUNING_NO_GM_CLASS')
    raise SystemExit(1)

cdo = unreal.get_default_object(cls)

for prop, value in TARGET_VALUES.items():
    try:
        old = cdo.get_editor_property(prop)
        cdo.set_editor_property(prop, value)
        new = cdo.get_editor_property(prop)
        unreal.log_warning(f'TUNING_SET {prop}: {old} -> {new}')
    except Exception as ex:
        unreal.log_warning(f'TUNING_SKIP {prop}: {ex}')

saved = unreal.EditorAssetLibrary.save_loaded_asset(bp)
unreal.log_warning(f'TUNING_SAVE_GM={saved}')
