import unreal
bp = unreal.EditorAssetLibrary.load_asset('/Game/FirstPerson/Blueprints/BP_FirstPersonCharacter')
if not bp:
    unreal.log_error('NO_BP')
    raise SystemExit(1)

unreal.log('TYPE=' + str(type(bp)))
for name in dir(bp):
    if 'component' in name.lower() or 'construction' in name.lower() or 'simple' in name.lower() or 'generated' in name.lower() or 'blueprint' in name.lower():
        unreal.log('ATTR ' + name)
