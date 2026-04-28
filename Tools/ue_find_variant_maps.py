import unreal
reg = unreal.AssetRegistryHelpers.get_asset_registry()
for d in reg.get_assets_by_path('/Game/Variant_Shooter_BP', recursive=True):
    if str(d.asset_class_path.asset_name) == 'World':
        unreal.log_warning(f'VARIANT_MAP {d.package_name}')
