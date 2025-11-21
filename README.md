# comfyui-excel-loader
Load embedded images and text directly from Excel (.xlsx) into ComfyUI. Automate batch workflows without managing local file paths.
# 🚀 ComfyUI Excel Media Loader

**一个专为“懒人”设计师打造的 ComfyUI 节点，直接读取 Excel 表格中嵌入的图片和文字，无需整理文件夹。**

> **English** | [中文](./README.md)

## 😭 你是否也遇到过这些问题？

* ❌ **素材整理噩梦：** 策划给的 Excel 表里贴满了参考图，还得一张张右键“另存为”？
* ❌ **路径地狱：** 为了跑批量图，还要把图片文件名一个个复制到 Excel 里做路径索引？
* ❌ **图片错位：** 改了文件名，ComfyUI 就找不到图了？

**ComfyUI Excel Media Loader** 完美解决以上痛点！它能直接“扣”出 Excel 单元格里的图片，并读取对应的提示词，让你的工作流从 Excel 直接启动。

---

## ✨ 核心功能 (Features)

* ✅ **嵌入式图片读取：** 真正支持读取 Excel 单元格内粘贴/嵌入的图片（基于 `openpyxl-image-loader`）。
* ✅ **零文件整理：** 不需要将图片导出为文件，不需要重命名，丢进去就能跑。
* ✅ **智能防崩：** 如果单元格里没图，自动生成黑色占位图，防止工作流报错中断。
* ✅ **批量自动化：** 配合 Primitive 节点，轻松实现“点击一次，自动遍历 Excel 所有行”的批量出图。

---

## 🛠️ 安装指南 (Installation)

### 方法 1：使用 ComfyUI Manager (推荐)
*(等待上架中...目前请使用方法 2)*

### 方法 2：手动安装
1. 进入你的 ComfyUI `custom_nodes` 目录：
   ```bash
   cd ComfyUI/custom_nodes/
