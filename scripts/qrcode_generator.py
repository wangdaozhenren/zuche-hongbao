#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""qrcode_generator.py — 二维码生成器
将红包链接生成为二维码图片，方便客户用手机扫码领取。
依赖: pip install qrcode[pil]
用法: python qrcode_generator.py --url "https://..." --output "qrcode.png" [--size 10]
"""
import argparse
import os
import sys


def generate(url, output, size=10, border=2):
    try:
        import qrcode
    except ImportError:
        print("请先安装依赖: pip install qrcode[pil]", file=sys.stderr)
        sys.exit(1)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    os.makedirs(os.path.dirname(output) or ".", exist_ok=True)
    img.save(output)
    print(f"二维码已生成: {output}")
    return output


def main():
    ap = argparse.ArgumentParser(description="二维码生成器")
    ap.add_argument("--url", required=True, help="要生成二维码的链接")
    ap.add_argument("--output", required=True, help="输出图片路径(.png)")
    ap.add_argument("--size", type=int, default=10, help="二维码格子大小(默认10)")
    ap.add_argument("--border", type=int, default=2, help="边框宽度(默认2)")
    args = ap.parse_args()
    generate(args.url, args.output, args.size, args.border)


if __name__ == "__main__":
    main()
