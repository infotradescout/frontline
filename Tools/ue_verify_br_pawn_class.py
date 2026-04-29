import unreal

CLASS_PATH = "/Script/FrontlineWarfare.FrontlineBRGameMode"

cls = unreal.load_class(None, CLASS_PATH)
if not cls:
    unreal.log_error(f"BR_PAWN_VERIFY_CLASS_MISSING {CLASS_PATH}")
    raise SystemExit(1)

cdo = unreal.get_default_object(cls)
pawn_cls = cdo.get_editor_property("default_pawn_class")
name = pawn_cls.get_path_name() if pawn_cls else "None"
unreal.log_warning(f"BR_PAWN_DEFAULT {name}")
