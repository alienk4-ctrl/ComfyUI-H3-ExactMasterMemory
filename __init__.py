from .nodes import (
    NODE_CLASS_MAPPINGS as _MEM_CLASSES,
    NODE_DISPLAY_NAME_MAPPINGS as _MEM_NAMES,
)
from .keyframes_stable import (
    NODE_CLASS_MAPPINGS as _KF_CLASSES,
    NODE_DISPLAY_NAME_MAPPINGS as _KF_NAMES,
)
from .ui_utils import (
    NODE_CLASS_MAPPINGS as _UI_CLASSES,
    NODE_DISPLAY_NAME_MAPPINGS as _UI_NAMES,
)
from .semantic_ref import (
    NODE_CLASS_MAPPINGS as _SEM_CLASSES,
    NODE_DISPLAY_NAME_MAPPINGS as _SEM_NAMES,
)

VERSION = "0.4.3"

NODE_CLASS_MAPPINGS = {
    **_MEM_CLASSES,
    **_KF_CLASSES,
    **_UI_CLASSES,
    **_SEM_CLASSES,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    **_MEM_NAMES,
    **_KF_NAMES,
    **_UI_NAMES,
    **_SEM_NAMES,
}

print(
    "[H3ExactMasterMemory] v0.4.3 loaded | "
    "ExactMaster + StableKeyframes + Workflow UI + Semantic REF2VA registered",
    flush=True,
)

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
