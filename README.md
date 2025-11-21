# 📊 ComfyUI Excel Loader

> **Seamlessly load embedded images and prompts from Excel to ComfyUI.**
>
> **无缝读取 Excel 嵌入图片与提示词，专为 ComfyUI 批量化工作流设计。**

[English](#english) | [中文](#chinese)

---

<a name="english"></a>
## 📖 English

### Introduction
**ComfyUI Excel Loader** is a custom node designed to streamline batch generation workflows. It allows users to read **embedded images** (pasted directly into cells) and text prompts from `.xlsx` files directly.

Unlike traditional loaders that require local file paths, this tool extracts image data directly from the spreadsheet, eliminating the need for manual file management and path referencing.

### ✨ Key Features
* **Embedded Image Extraction:** Uses `openpyxl-image-loader` to retrieve images directly pasted into Excel cells.
* **Path-Free Workflow:** No need to maintain a local folder structure or copy-paste file paths.
* **Batch Processing Ready:** Designed to work with ComfyUI's primitive increment system for automated batch generation.
* **Error Handling:** Automatically generates a placeholder image (black tensor) if a cell is empty, ensuring the workflow does not crash during batch runs.

### 🛠️ Installation

1.  Navigate to your ComfyUI `custom_nodes` directory:
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  Clone this repository:
    ```bash
    git clone [https://github.com/realruian/comfyui-excel-loader.git](https://github.com/realruian/comfyui-excel-loader.git)
    ```
3.  **Important:** Install the required dependencies (ensure you are in the ComfyUI virtual environment):
    ```bash
    pip install pandas openpyxl openpyxl-image-loader pillow
    ```

### ⚙️ Usage

1.  **Prepare Excel:**
    * Create an `.xlsx` file.
    * **Column A (example):** Text prompts.
    * **Column B (example):** Paste/Insert images directly into cells.
    * *Note: Ensure images are contained within the cell boundaries.*
2.  **Add Node:**
    * Search for **`Excel Embedded Image Loader`** in ComfyUI.
3.  **Configure Parameters:**
    * `excel_path`: Absolute path to your `.xlsx` file.
    * `row_index`: The row number to read (starting from 1).
    * `image_column`: Column letter for images (e.g., "B").
    * `text_column`: Column letter for text (e.g., "A").

---

<a name="chinese"></a>
## 🇨🇳 中文说明

### 简介
**ComfyUI Excel Loader** 是一个专为提升 AIGC 生产效率而设计的自定义节点。它支持直接读取 Excel (`.xlsx`) 表格中**嵌入/粘贴的图片**以及对应的文本提示词。

传统的批量工作流通常需要整理复杂的本地图片路径，而本工具直接解析 Excel 内部数据，无需管理文件路径，极大简化了从“策划文档”到“批量出图”的流程。

### ✨ 核心功能
* **嵌入式图片读取：** 基于 `openpyxl` 技术，直接提取单元格内粘贴的图片对象。
* **零路径管理：** 彻底告别“右键另存为”和“复制文件路径”的繁琐操作。
* **批量自动化：** 完美适配 ComfyUI 的 Primitive 递增机制，实现全自动遍历表格出图。
* **健壮性设计：** 内置异常处理机制，若检测到空单元格，将自动生成黑色占位图，防止批量任务意外中断。

### 🛠️ 安装指南

1.  进入 ComfyUI 的 `custom_nodes` 目录：
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  克隆本项目：
    ```bash
    git clone [https://github.com/realruian/comfyui-excel-loader.git](https://github.com/realruian/comfyui-excel-loader.git)
    ```
3.  **安装依赖（必选）：**
    请确保在 ComfyUI 的 Python 环境中运行以下命令：
    ```bash
    pip install pandas openpyxl openpyxl-image-loader pillow
    ```

### ⚙️ 使用方法

1.  **准备 Excel 文件：**
    * 新建 `.xlsx` 文件。
    * **A列 (示例)：** 输入提示词。
    * **B列 (示例)：** 直接**粘贴**或**插入**参考图。
    * *注意：为确保识别准确，建议将单元格拉大，使图片完全位于单元格边框内。*
2.  **添加节点：**
    * 在 ComfyUI 中搜索并添加 **`Excel Embedded Image Loader`**。
3.  **参数设置：**
    * `excel_path`: Excel 文件的绝对路径。
    * `row_index`: 指定读取的行号（从 1 开始）。
        * *提示：将此参数转换为 Input 并连接 Primitive 节点（设置为 Increment），即可实现批量循环。*
    * `image_column`: 图片所在的列号（如 "B"）。
    * `text_column`: 文字所在的列号（如 "A"）。

---

## 📄 License
MIT License
