import unreal

TARGETS = [
    '/Game/Variant_Shooter/Blueprints/BP_ShooterGameMode',
    '/Game/Variant_Shooter/Blueprints/BP_ShooterPlayerController',
    '/Game/Variant_Shooter/Blueprints/BP_ShooterCharacter',
]

for p in TARGETS:
    bp = unreal.EditorAssetLibrary.load_asset(p)
    if not bp:
        unreal.log_warning(f'TARGET_MISSING {p}')
        continue

    cls = bp.generated_class()
    unreal.log_warning(f'TARGET {p} CLASS_OK={cls is not None}')
    if not cls:
        continue

    cdo = unreal.get_default_object(cls)
    # Dump all editable property names for fast tuning
    names = []
    for name in dir(cdo):
        if name.startswith('_'):
            continue
        names.append(name)

    # Filter likely gameplay/HUD properties
    keywords = ('score', 'kill', 'win', 'lose', 'hud', 'match', 'round', 'time', 'bot', 'respawn', 'spawn', 'health')
    likely = [n for n in names if any(k in n.lower() for k in keywords)]
    likely.sort()
    unreal.log_warning(f'LIKELY_PROPS {p} :: ' + ', '.join(likely[:200]))

    # Emit current value for likely properties if readable
    for n in likely[:200]:
        try:
            v = cdo.get_editor_property(n)
            unreal.log_warning(f'PROP_VAL {p}::{n}={v}')
        except Exception:
            pass
