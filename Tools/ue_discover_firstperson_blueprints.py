import unreal

registry = unreal.AssetRegistryHelpers.get_asset_registry()
assets = registry.get_assets_by_path('/Game/FirstPerson', recursive=True)

for data in assets:
    cls_name = str(data.asset_class_path.asset_name)
    if cls_name not in ('Blueprint', 'WidgetBlueprint'):
        continue
    name = str(data.asset_name)
    if 'GameMode' in name or 'Character' in name or 'Controller' in name or 'FirstPerson' in name:
        pkg = str(data.package_name)
        asset = str(data.asset_name)
        unreal.log_warning(f'BP_CANDIDATE {pkg}.{asset}')
