#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import math
import os
import sys
from typing import Tuple

from PIL import Image

# 按需导入（未安装也能处理位图）
try:
    from pdf2image import convert_from_path  # type: ignore

    _HAS_PDF = True
except Exception:
    _HAS_PDF = False

try:
    import cairosvg  # type: ignore

    _HAS_SVG = True
except Exception:
    _HAS_SVG = False


TARGET_W, TARGET_H = 5, 3  # 目标比例 5:3
TARGET_RATIO = TARGET_W / TARGET_H
FINAL_W, FINAL_H = 500, 300  # 最终导出分辨率（可按需改）


def _open_image_any(path: str) -> Image.Image:
    """
    打开任意受支持的图像：
    - 位图格式：直接用 PIL 打开
    - PDF：取第一页渲染为位图
    - SVG：栅格化为位图
    返回 PIL Image（统一 RGBA）
    """
    ext = os.path.splitext(path)[1].lower()

    if ext in [".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"]:
        im = Image.open(path).convert("RGBA")
        return im

    if ext == ".pdf":
        if not _HAS_PDF:
            raise RuntimeError(
                "检测到 PDF 输入，但未安装 pdf2image 或系统未配置 Poppler。"
            )
        pages = convert_from_path(path, dpi=300, first_page=1, last_page=1)
        if not pages:
            raise RuntimeError("未能从 PDF 读取到任何页面。")
        return pages[0].convert("RGBA")

    if ext == ".svg":
        if not _HAS_SVG:
            raise RuntimeError("检测到 SVG 输入，但未安装 cairosvg。")
        from io import BytesIO

        png_bytes = cairosvg.svg2png(url=path)
        return Image.open(BytesIO(png_bytes)).convert("RGBA")

    raise RuntimeError(f"不支持的文件类型：{ext}")


def _compute_canvas_size(w: int, h: int) -> Tuple[int, int]:
    """
    计算扩展到 5:3 的最小画布尺寸（仅增不减），原图不缩放：
    - 先试固定宽：h' = ceil(w * 3/5)，若 h' >= h -> (w, h') 上下补白
    - 否则固定高：w' = ceil(h * 5/3) -> (w', h) 左右补白
    """
    target_h_from_w = math.ceil(w * (TARGET_H / TARGET_W))
    if target_h_from_w >= h:
        return w, target_h_from_w
    target_w_from_h = math.ceil(h * (TARGET_W / TARGET_H))
    return target_w_from_h, h


def _paste_center(bg: Image.Image, fg: Image.Image) -> Image.Image:
    """将前景图像居中粘贴到背景（RGBA）。"""
    bg_w, bg_h = bg.size
    fg_w, fg_h = fg.size
    x = (bg_w - fg_w) // 2
    y = (bg_h - fg_h) // 2
    bg.alpha_composite(fg, (x, y))
    return bg


def pad_to_5_3(input_path: str, output_path: str, resize_final: bool = True) -> None:
    im = _open_image_any(input_path)  # RGBA
    w, h = im.size

    # 已经是 5:3（允许微误差）则直接采用原尺寸作为画布
    if abs((w / h) - TARGET_RATIO) < 1e-6:
        canvas_w, canvas_h = w, h
    else:
        canvas_w, canvas_h = _compute_canvas_size(w, h)

    # 白底画布
    bg = Image.new("RGBA", (canvas_w, canvas_h), (255, 255, 255, 255))
    result = _paste_center(bg, im)

    # 按需统一缩放到 500x300（保持 5:3 无变形）
    if resize_final:
        result = result.resize((FINAL_W, FINAL_H), resample=Image.LANCZOS)

    # 根据输出扩展名决定是否丢弃透明通道（JPEG 无透明）
    ext = os.path.splitext(output_path)[1].lower()
    if ext in [".jpg", ".jpeg"]:
        result = result.convert("RGB")

    # 确保输出目录存在
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    result.save(output_path)

    final_w, final_h = result.size
    print(
        f"✅ 已保存：{output_path}  （画布尺寸：{canvas_w}x{canvas_h} -> 输出尺寸：{final_w}x{final_h}）"
    )


def _default_output_path(input_path: str) -> str:
    base, _ext = os.path.splitext(input_path)
    return base + "_new.png"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="将输入图片/PDF/SVG 通过补白扩展为 5:3 画布并可统一缩放到 500x300，原图不缩放不裁剪并居中。"
    )
    p.add_argument(
        "-i",
        "--input_image",
        required=True,
        help="输入文件路径（png/jpg/jpeg/webp/bmp/tif/tiff/svg/pdf）",
    )
    p.add_argument(
        "-o",
        "--output_image",
        required=False,
        help="输出文件路径（默认：原文件名 + _new.png）",
    )
    # 默认开启：--resize_final；如需关闭：--no-resize_final
    group = p.add_mutually_exclusive_group()
    group.add_argument(
        "--resize_final",
        dest="resize_final",
        action="store_true",
        help="在补白到 5:3 后统一缩放到 500x300（默认开启）",
    )
    group.add_argument(
        "--no-resize_final",
        dest="resize_final",
        action="store_false",
        help="关闭统一缩放，保持补白后的原始像素尺寸",
    )
    p.set_defaults(resize_final=True)
    return p.parse_args()


def main() -> None:
    args = parse_args()
    in_path = args.input_image
    if not os.path.isfile(in_path):
        print(f"❌ 找不到输入文件：{in_path}", file=sys.stderr)
        sys.exit(1)

    out_path = args.output_image or _default_output_path(in_path)
    try:
        pad_to_5_3(in_path, out_path, resize_final=args.resize_final)
    except Exception as e:
        print(f"❌ 处理失败：{e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
