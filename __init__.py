from .nodes import ExcelEmbeddedImageNode

NODE_CLASS_MAPPINGS = {
    "ExcelEmbeddedImageNode": ExcelEmbeddedImageNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ExcelEmbeddedImageNode": "Excel Embedded Image Loader",
}

__all__ = ["ExcelEmbeddedImageNode", "NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
