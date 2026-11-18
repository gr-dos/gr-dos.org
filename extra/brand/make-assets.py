#!/usr/bin/env python3
"""Make the website's images from the master artwork.

    extra/brand/make-assets.py

Reads   design/Charcoal Vintage Floppy Disk.png   (the approved floppy)
        extra/screen/gr-dos-screen.png             (from extra/screen/capture.py)
Writes  docs/images/gr-dos-floppy.png        large floppy, transparent background
        docs/images/gr-dos-floppy-icon.png   small floppy for the header
        docs/images/gr-dos-screen-crt.png    the screenshot in a beige CRT
        docs/images/gr-dos-social.png        1200x630 social preview card
        docs/apple-touch-icon.png            180x180, on the artwork's cream
        docs/favicon.ico                     16, 32 and 48 px

Needs Pillow and the DejaVu Sans font.
"""

import os
from collections import deque

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MASTER = os.path.join(ROOT, "design", "Charcoal Vintage Floppy Disk.png")
SCREEN = os.path.join(ROOT, "extra", "screen", "gr-dos-screen.png")
IMAGES = os.path.join(ROOT, "docs", "images")
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

CREAM = (253, 231, 192)   # the artwork's background
TOLERANCE = 60            # how far from CREAM still counts as background


def dist(a, b):
    return max(abs(x - y) for x, y in zip(a, b))


def color_to_alpha(p, bg, floor=0.12):
    """Like GIMP's colour-to-alpha, but only for colours darker than bg (the
    shadow and the disk's anti-aliased edge), and treating the slight
    variation of the cream paper texture (under floor) as fully transparent."""
    alpha = max((b - c) / b for c, b in zip(p, bg))
    if alpha <= floor:
        return (0, 0, 0, 0)
    alpha = min(1.0, (alpha - floor) / (1 - floor))
    # the colour that, at this alpha over bg, gives p
    rgb = tuple(max(0, min(255, round((c - b * (1 - alpha)) / alpha)))
                for c, b in zip(p, bg))
    return rgb + (round(alpha * 255),)


def cut_out(im):
    """Make the cream background transparent.  Only pixels joined to the
    image's edge (the surround, the write-protect notch) or to the hub's
    centre hole are touched, so the cream paper label is left alone.  The
    blue shadow and anti-aliased edges keep their partial transparency."""
    w, h = im.size
    px = im.load()
    seen = bytearray(w * h)
    q = deque()
    seeds = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1), (w // 2, h * 51 // 100)]
    for s in seeds:
        q.append(s)
        seen[s[1] * w + s[0]] = 1
    region = []
    while q:
        x, y = q.popleft()
        region.append((x, y))
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and not seen[ny * w + nx]:
                seen[ny * w + nx] = 1
                c = px[nx, ny]
                # cream background, or the light blue shadow on it
                if dist(c, CREAM) <= TOLERANCE or (c[2] > c[0] + 40 and sum(c) > 300):
                    q.append((nx, ny))
    # Grow the region by a couple of pixels to catch the edges' fringe.
    region_mask = Image.new("L", (w, h), 0)
    rm = region_mask.load()
    for x, y in region:
        rm[x, y] = 255
    region_mask = region_mask.filter(ImageFilter.MaxFilter(5))
    rm = region_mask.load()
    out = im.convert("RGBA")
    op = out.load()
    for y in range(h):
        for x in range(w):
            if rm[x, y]:
                op[x, y] = color_to_alpha(px[x, y], CREAM)
    return out


def crop_to_content(im, pad=8):
    box = im.getchannel("A").point(lambda a: 255 if a > 8 else 0).getbbox()
    box = (max(0, box[0] - pad), max(0, box[1] - pad),
           min(im.width, box[2] + pad), min(im.height, box[3] + pad))
    return im.crop(box)


def fit(im, size):
    """Scale im to fit in a size x size square, centred."""
    im = im.copy()
    im.thumbnail((size, size), Image.LANCZOS)
    sq = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    sq.paste(im, ((size - im.width) // 2, (size - im.height) // 2), im)
    return sq


def vgrad(draw, box, top, bottom, radius):
    """A rounded rectangle with a vertical gradient (drawn line by line
    through a mask)."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    grad = Image.new("RGB", (w, h))
    gd = ImageDraw.Draw(grad)
    for y in range(h):
        t = y / max(1, h - 1)
        gd.line([(0, y), (w, y)], fill=tuple(round(a + (b - a) * t) for a, b in zip(top, bottom)))
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, w - 1, h - 1), radius, fill=255)
    draw._image.paste(grad, (x0, y0), mask)


def hex2rgb(s):
    return tuple(int(s[i:i + 2], 16) for i in (1, 3, 5))


def crt(screen, icon):
    """Frame the 720x400 screenshot in a beige CRT, after
    ticoedit.org's extra/crt/crt.svg.in.  Drawn at 2x and scaled down for
    smooth edges; the screenshot is pasted at 1:1 afterwards."""
    S = 2
    sw, sh = screen.size
    m = 40                       # glass to case edge
    W, H = sw + 2 * m, sh + m + 74
    total_h = H + 58             # with the stand
    im = Image.new("RGBA", (W * S, total_h * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    case_top, case_bot = hex2rgb("#fdfcf8"), hex2rgb("#e4e0d5")
    edge = hex2rgb("#b9b4a7")
    # stand
    cx = W // 2
    d.polygon([((cx - 80) * S, (H - 2) * S), ((cx + 80) * S, (H - 2) * S),
               ((cx + 104) * S, (H + 30) * S), ((cx - 104) * S, (H + 30) * S)],
              fill=hex2rgb("#dcd8cc"), outline=edge, width=2 * S)
    d.rounded_rectangle(((cx - 190) * S, (H + 24) * S, (cx + 190) * S, (H + 52) * S),
                        10 * S, fill=hex2rgb("#ece9e0"), outline=edge, width=2 * S)
    # case, recess and glass surround
    d.rounded_rectangle((0, 0, W * S - 1, H * S - 1), 30 * S, fill=edge)
    vgrad(d, (2 * S, 2 * S, (W - 2) * S, (H - 2) * S), case_top, case_bot, 28 * S)
    vgrad(d, (20 * S, 18 * S, (W - 20) * S, (m + sh + 22) * S),
          hex2rgb("#c9c4b7"), hex2rgb("#ebe8df"), 20 * S)
    d.rounded_rectangle((30 * S, 28 * S, (W - 30) * S, (m + sh + 10) * S), 14 * S,
                        fill=hex2rgb("#141414"))
    # power light and button
    d.rounded_rectangle(((W - 114) * S, (H - 34) * S, (W - 74) * S, (H - 22) * S), 3 * S,
                        fill=hex2rgb("#d6d2c6"), outline=hex2rgb("#bdb8ab"), width=S)
    d.ellipse(((W - 59) * S, (H - 33) * S, (W - 49) * S, (H - 23) * S),
              fill=hex2rgb("#4cd964"), outline=hex2rgb("#2f9e44"), width=S)
    im = im.resize((W, total_h), Image.LANCZOS)
    # glass: the screenshot, with rounded corners
    mask = Image.new("L", screen.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, sw - 1, sh - 1), 8, fill=255)
    im.paste(screen.convert("RGB"), (m, m - 2), mask)
    # badge
    badge = fit(icon, 28)
    im.alpha_composite(badge, (44, H - 42))
    ImageDraw.Draw(im).text((80, H - 39), "GR-DOS", font=ImageFont.truetype(FONT, 18),
                            fill=hex2rgb("#9c978a"))
    return im


def main():
    os.makedirs(IMAGES, exist_ok=True)
    master = Image.open(MASTER).convert("RGB")
    floppy = crop_to_content(cut_out(master))

    big = floppy.copy()
    big.thumbnail((640, 640), Image.LANCZOS)
    # A 256-colour palette makes it a tenth of the size, with no visible loss.
    big.quantize(256, method=Image.Quantize.FASTOCTREE).save(
        os.path.join(IMAGES, "gr-dos-floppy.png"), optimize=True)

    icon = fit(floppy, 128)
    icon.save(os.path.join(IMAGES, "gr-dos-floppy-icon.png"), optimize=True)

    ico = [fit(floppy, s) for s in (48, 32, 16)]
    ico[0].save(os.path.join(ROOT, "docs", "favicon.ico"), sizes=[(48, 48), (32, 32), (16, 16)],
                append_images=ico[1:])

    touch = master.copy()
    touch.thumbnail((180, 180), Image.LANCZOS)
    touch.save(os.path.join(ROOT, "docs", "apple-touch-icon.png"), optimize=True)

    screen = Image.open(SCREEN)
    monitor = crt(screen, floppy)
    monitor.save(os.path.join(IMAGES, "gr-dos-screen-crt.png"), optimize=True)

    social = Image.new("RGBA", (1200, 630), CREAM + (255,))
    f = floppy.copy()
    f.thumbnail((520, 520), Image.LANCZOS)
    social.alpha_composite(f, (50, (630 - f.height) // 2))
    mon = monitor.copy()
    mon.thumbnail((560, 560), Image.LANCZOS)
    social.alpha_composite(mon, (600, (630 - mon.height) // 2))
    social.convert("RGB").quantize(256).save(os.path.join(IMAGES, "gr-dos-social.png"), optimize=True)

    for name in ("images/gr-dos-floppy.png", "images/gr-dos-floppy-icon.png",
                 "images/gr-dos-screen-crt.png", "images/gr-dos-social.png",
                 "apple-touch-icon.png", "favicon.ico"):
        path = os.path.join(ROOT, "docs", name)
        print(f"wrote docs/{name} ({os.path.getsize(path)} bytes)")


if __name__ == "__main__":
    main()
