#!/usr/bin/env python3
"""Render the LS monogram favicon from the site's own display face.

Outputs an ink tile with the paper-coloured monogram — the site's palette
inverted, so the mark still reads at 16px against a light browser tab.

    python3 scripts/build-favicon.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "src/fonts/ArchivoExpanded-ExtraBold.ttf"
PUBLIC = ROOT / "public"

INK = (22, 33, 27)
PAPER = (233, 237, 228)

TEXT = "LS"
# Fraction of the tile the monogram should span horizontally.
FILL = 0.78


def render(size: int) -> Image.Image:
    # Supersample, then downscale — keeps the counters crisp at small sizes.
    scale = 8 if size < 128 else 2
    px = size * scale

    img = Image.new("RGB", (px, px), INK)
    draw = ImageDraw.Draw(img)

    # Binary-search the point size that makes TEXT span FILL of the tile.
    lo, hi = 1, px * 2
    font = ImageFont.truetype(str(FONT), lo)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        candidate = ImageFont.truetype(str(FONT), mid)
        left, top, right, bottom = candidate.getbbox(TEXT)
        if (right - left) <= px * FILL and (bottom - top) <= px * FILL:
            font, lo = candidate, mid
        else:
            hi = mid - 1

    # Centre on the ink bounding box, not the font's line box, so the
    # monogram sits optically centred rather than sitting on the baseline.
    left, top, right, bottom = font.getbbox(TEXT)
    x = (px - (right - left)) / 2 - left
    y = (px - (bottom - top)) / 2 - top
    draw.text((x, y), TEXT, font=font, fill=PAPER)

    return img.resize((size, size), Image.LANCZOS)


def main() -> None:
    PUBLIC.mkdir(exist_ok=True)

    # Multi-resolution .ico for legacy browsers and Windows tiles.
    render(64).save(
        PUBLIC / "favicon.ico",
        sizes=[(16, 16), (32, 32), (48, 48), (64, 64)],
    )

    for size, name in [(32, "favicon-32.png"), (180, "apple-touch-icon.png"), (512, "icon-512.png")]:
        render(size).save(PUBLIC / name)
        print(f"wrote public/{name}")

    print("wrote public/favicon.ico")


if __name__ == "__main__":
    main()
