import unreal
reg = unreal.AssetRegistryHelpers.get_asset_registry()
for p in ('/Game/FirstPerson','/Game/Input'):
    for d in reg.get_assets_by_path(p, recursive=True):
        n=str(d.asset_name)
        if n.startswith('IA_') or n.startswith('IMC_') or 'Input' in n or 'Mapping' in n:
            unreal.log_warning(f'ASSET {d.package_name} CLASS={d.asset_class_path.asset_name}')
