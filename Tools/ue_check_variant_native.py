import unreal

paths = [
    '/Game/Variant_Shooter/Blueprints/BP_ShooterCharacter',
    '/Game/Variant_Shooter/Blueprints/BP_ShooterGameMode',
    '/Game/Variant_Shooter/Blueprints/BP_ShooterPlayerController',
    '/Game/Variant_Shooter/Lvl_ArenaShooter',
]

for p in paths:
    a = unreal.EditorAssetLibrary.load_asset(p)
    exists = a is not None
    cls_ok = False
    if exists and hasattr(a, 'generated_class'):
        try:
            cls_ok = a.generated_class() is not None
        except Exception:
            cls_ok = False
    unreal.log_warning(f'NATIVE_VARIANT {p} EXISTS={exists} CLASS_OK={cls_ok}')
