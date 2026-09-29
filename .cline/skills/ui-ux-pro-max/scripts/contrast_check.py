#!/usr/bin/env python3
"""Check WCAG contrast ratio between a foreground and background color.

Usage:
    python contrast_check.py --fg "#333333" --bg "#ffffff"

Accepts hex colors (#rgb, #rrggbb, with or without '#'). Prints the contrast
ratio and whether foreground/background pairs meet WCAG AA/AAA thresholds.
Exit code 0 always (informational); ratio printed to stdout.
"""

import argparse
import re


def hex_to_rgb(value: str) -> list[int]:
    value = value.strip().lstrip("#")
    if len(value) == 3:
        value = "".join(c * 2 for c in value)
    if not re.fullmatch(r"[0-9a-fA-F]{6}", value):
        raise ValueError(f"Invalid hex color: {value}")
    return [int(value[i : i + 2], 16) for i in (0, 2, 4)]


def luminance(rgb: list[int]) -> float:
    def channel(c: int) -> float:
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (channel(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg: list[int], bg: list[int]) -> float:
    l1, l2 = luminance(fg), luminance(bg)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute WCAG contrast ratio.")
    parser.add_argument("--fg", required=True, help="Foreground (text) color, e.g. #333333")
    parser.add_argument("--bg", required=True, help="Background color, e.g. #ffffff")
    args = parser.parse_args()

    try:
        fg = hex_to_rgb(args.fg)
        bg = hex_to_rgb(args.bg)
    except ValueError as e:
        print(f"Error: {e}")
        return

    ratio = contrast_ratio(fg, bg)
    print(f"FG {args.fg} on BG {args.bg}")
    print(f"Contrast ratio: {ratio:.2f}:1")
    print(f"  WCAG AA normal text   (>=4.5): {'PASS' if ratio >= 4.5 else 'FAIL'}")
    print(f"  WCAG AA large text    (>=3.0): {'PASS' if ratio >= 3.0 else 'FAIL'}")
    print(f"  WCAG AAA normal text  (>=7.0): {'PASS' if ratio >= 7.0 else 'FAIL'}")


if __name__ == "__main__":
    main()
