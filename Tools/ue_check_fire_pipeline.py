import unreal

assets_to_check = [
    '/Game/Input/Actions/IA_Fire',
    '/Game/Input/IMC_Default',
    '/Game/FirstPerson/Blueprints/BP_FirstPersonCharacter',
    '/Game/FirstPerson/Blueprints/BP_FirstPersonPlayerController',
    '/Game/FirstPerson/Blueprints/BP_FirstPersonGameMode',
]

for path in assets_to_check:
    obj = unreal.EditorAssetLibrary.load_asset(path)
    unreal.log_warning(f'PIPELINE_ASSET {path} EXISTS={obj is not None}')
    if obj is not None:
        refs = unreal.EditorAssetLibrary.find_package_referencers_for_asset(path, load_assets_to_confirm=False)
        unreal.log_warning(f'PIPELINE_REFS {path} COUNT={len(refs)}')

# Dump all assets under /Game/Input and legacy /Game/FirstPerson/Input
registry = unreal.AssetRegistryHelpers.get_asset_registry()
for data in registry.get_assets_by_path('/Game/Input', recursive=True):
    unreal.log_warning(f'INPUT_ASSET {data.package_name} CLASS={data.asset_class_path.asset_name}')

for data in registry.get_assets_by_path('/Game/FirstPerson/Input', recursive=True):
    unreal.log_warning(f'INPUT_ASSET {data.package_name} CLASS={data.asset_class_path.asset_name}')
