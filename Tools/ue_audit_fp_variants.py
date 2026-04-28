import unreal

ROOT = '/Game/FirstPerson/Blueprints'

registry = unreal.AssetRegistryHelpers.get_asset_registry()
assets = registry.get_assets_by_path(ROOT, recursive=True)

candidates = []
for data in assets:
    cls_name = str(data.asset_class_path.asset_name)
    if cls_name != 'Blueprint':
        continue
    asset_name = str(data.asset_name)
    pkg_name = str(data.package_name)
    if asset_name in ('BP_FirstPersonCharacter', 'BP_FirstPersonGameMode', 'BP_FirstPersonPlayerController'):
        candidates.append((asset_name, pkg_name))

for asset_name, pkg in sorted(candidates):
    bp = unreal.EditorAssetLibrary.load_asset(pkg)
    gen = bp.generated_class() if bp else None
    unreal.log_warning(f'AUDIT_BP {asset_name} PATH={pkg} CLASS_OK={gen is not None}')
    if asset_name == 'BP_FirstPersonCharacter' and gen is not None:
        cdo = unreal.get_default_object(gen)
        names = []
        try:
            for comp in cdo.get_components_by_class(unreal.ActorComponent):
                names.append(comp.get_name())
        except Exception:
            pass
        names.sort()
        unreal.log_warning('AUDIT_CHAR_COMPONENTS ' + pkg + ' :: ' + ', '.join(names[:40]))

# Also list FirstPerson maps under /Game/FirstPerson
map_assets = registry.get_assets_by_path('/Game/FirstPerson', recursive=True)
for data in map_assets:
    if str(data.asset_class_path.asset_name) == 'World':
        unreal.log_warning(f'AUDIT_MAP {data.package_name}')
