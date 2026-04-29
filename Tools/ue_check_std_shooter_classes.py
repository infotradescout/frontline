import unreal

paths = [
    '/Game/Variant_Shooter_Std/Blueprints/BP_ShooterCharacter',
    '/Game/Variant_Shooter_Std/Blueprints/BP_ShooterGameMode',
    '/Game/Variant_Shooter_Std/Blueprints/BP_ShooterPlayerController',
]

for p in paths:
    bp = unreal.EditorAssetLibrary.load_asset(p)
    if not bp:
        unreal.log_warning(f'NO_ASSET {p}')
        continue
    cls = bp.generated_class()
    unreal.log_warning(f'CHECK {p} GENERATED_CLASS={cls}')
