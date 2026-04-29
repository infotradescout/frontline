import unreal

IA_PATH = '/Game/Input/Actions/IA_Fire'
IMC_PATH = '/Game/Input/IMC_Default'


def load(path: str):
    asset = unreal.EditorAssetLibrary.load_asset(path)
    unreal.log_warning(f'FIRE_FIX_CHECK {path} EXISTS={asset is not None}')
    return asset


def ensure_fire_action():
    ia = load(IA_PATH)
    if ia is not None:
        return ia

    # Some UE Python environments do not expose InputActionFactory.
    # Duplicate IA_Jump as a robust fallback to create IA_Fire.
    src = '/Game/Input/Actions/IA_Jump'
    src_obj = load(src)
    if src_obj is None:
        unreal.log_error('FIRE_FIX_SOURCE_IA_JUMP_MISSING')
        raise SystemExit(1)

    duplicated = unreal.EditorAssetLibrary.duplicate_asset(src, IA_PATH)
    if not duplicated:
        unreal.log_error('FIRE_FIX_DUPLICATE_IA_FAIL')
        raise SystemExit(1)

    ia = load(IA_PATH)
    if ia is None:
        unreal.log_error('FIRE_FIX_CREATE_IA_FAIL')
        raise SystemExit(1)

    try:
        ia.set_editor_property('value_type', unreal.EInputActionValueType.BOOLEAN)
    except Exception as ex:
        unreal.log_warning(f'FIRE_FIX_SET_VALUE_TYPE_SKIP {ex}')

    saved = unreal.EditorAssetLibrary.save_loaded_asset(ia)
    unreal.log_warning(f'FIRE_FIX_CREATE_IA_OK SAVE={saved}')
    return ia


def ensure_mapping(imc, action):
    if not imc:
        unreal.log_error('FIRE_FIX_NO_IMC_DEFAULT')
        raise SystemExit(1)

    exists = False
    preferred_key = None
    try:
        mappings = imc.get_mappings()
        for m in mappings:
            if m.action == action:
                exists = True
            # Prefer the key currently used by IA_Jump if present
            try:
                if m.action and m.action.get_path_name() == '/Game/Input/Actions/IA_Jump.IA_Jump':
                    preferred_key = m.key
            except Exception:
                pass

        if preferred_key is None and len(mappings) > 0:
            preferred_key = mappings[0].key
    except Exception as ex:
        unreal.log_warning(f'FIRE_FIX_READ_MAPPINGS_FAIL {ex}')

    if exists:
        unreal.log_warning('FIRE_FIX_MAP_ALREADY_PRESENT')
    else:
        if preferred_key is not None:
            try:
                imc.map_key(action, preferred_key)
                unreal.log_warning(f'FIRE_FIX_MAP_ADDED IA_Fire -> {preferred_key}')
            except Exception as ex:
                unreal.log_warning(f'FIRE_FIX_MAP_ADD_FAIL {ex}')
        else:
            unreal.log_warning('FIRE_FIX_MAP_SKIP_NO_KEY_AVAILABLE')

    saved = unreal.EditorAssetLibrary.save_loaded_asset(imc)
    unreal.log_warning(f'FIRE_FIX_SAVE_IMC {saved}')


def main():
    ia = ensure_fire_action()
    imc = load(IMC_PATH)
    ensure_mapping(imc, ia)
    unreal.log_warning('FIRE_FIX_COMPLETE')


if __name__ == '__main__':
    main()
