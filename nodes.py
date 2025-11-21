import os
from typing import Tuple

import numpy as np
import torch
from PIL import Image
from openpyxl import load_workbook
from openpyxl_image_loader import SheetImageLoader


class ExcelEmbeddedImageNode:
    """从 Excel 行中提取嵌入图片与文本的 ComfyUI 节点"""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "excel_path": ("STRING", {"multiline": False, "default": ""}),
                "row_index": ("INT", {"default": 2, "min": 1, "max": 999999}),
                "image_column": ("STRING", {"default": "B"}),
                "text_column": ("STRING", {"default": "A"}),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("image", "text")
    FUNCTION = "load_excel_row"
    CATEGORY = "Excel"

    def load_excel_row(
        self, excel_path: str, row_index: int, image_column: str, text_column: str
    ) -> Tuple[torch.Tensor, str]:
        excel_path = excel_path.strip()
        if not excel_path:
            raise ValueError("Excel 路径不能为空")

        if not os.path.isfile(excel_path):
            raise FileNotFoundError(f"未找到 Excel 文件: {excel_path}")

        image_column = image_column.strip().upper() or "B"
        text_column = text_column.strip().upper() or "A"

        wb = load_workbook(excel_path, data_only=True)
        sheet = wb.active

        text_cell = f"{text_column}{row_index}"
        text_value = sheet[text_cell].value
        text_output = str(text_value) if text_value is not None else ""

        loader = SheetImageLoader(sheet)
        image_cell = f"{image_column}{row_index}"

        pil_image = self._load_or_placeholder(loader, image_cell)
        image_tensor = self._pil_to_tensor(pil_image)

        return image_tensor, text_output

    @staticmethod
    def _load_or_placeholder(loader: SheetImageLoader, cell_ref: str) -> Image.Image:
        try:
            if hasattr(loader, "image_in") and not loader.image_in(cell_ref):
                raise ValueError("no image")
            image = loader.get(cell_ref)
        except Exception:
            image = Image.new("RGB", (512, 512), color=(0, 0, 0))
        else:
            image = image.convert("RGB")
        return image

    @staticmethod
    def _pil_to_tensor(image: Image.Image) -> torch.Tensor:
        np_image = np.array(image).astype(np.float32) / 255.0
        if np_image.ndim == 2:
            np_image = np.stack([np_image] * 3, axis=-1)
        batch_image = np_image[None, ...]
        return torch.from_numpy(batch_image.copy())
