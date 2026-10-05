# -*- coding: utf-8 -*-
"""Build Helcurt Collector Widgets CSS."""
from pathlib import Path
SRC = Path(r"D:/KUMPULAN TUGAS/custom alert/35-rayquaza-pokemon/widgets")
DST = Path(r"D:/KUMPULAN TUGAS/helcurt-collector-alert/widgets")
DST.mkdir(exist_ok=True)

def transform_css(css_text):
    # ganti warna Rayquaza (#4be08a dll) ke Helcurt Collector (#e91e63, #2d0b40, #00e5ff)
    # juga ganti prefix rq35- jadi helc-
    t = css_text
    t = t.replace("rq35-", "helc-")
    # Case insensitive replacements for hexes
    repls = [
        ("#4be08a", "#e91e63"), ("#4BE08A", "#e91e63"),
        ("#062a33", "#2d0b40"), ("#062A33", "#2d0b40"),
        ("#03191f", "#1a0526"), ("#03191F", "#1a0526"),
        ("#053543", "#3b1152"), ("#053543", "#3b1152"),
        ("#12718f", "#7b1fa2"), ("#12718F", "#7b1fa2"),
        ("#ffc93c", "#00e5ff"), ("#FFC93C", "#00e5ff"),
        ("#ffe49b", "#84ffff"), ("#FFE49B", "#84ffff"),
        ("#ff6b4a", "#ff4081"), ("#FF6B4A", "#ff4081"),
        ("#f0fff6", "#fce4ec"), ("#F0FFF6", "#fce4ec"),
        ("#e7fff4", "#f8bbd0"), ("#E7FFF4", "#f8bbd0"),
        ("RAYQUAZA", "HELCURT COLLECTOR"),
        ("Rayquaza", "Helcurt Collector"),
        ("rayquaza", "helcurt collector"),
    ]
    for old, new in repls:
        t = t.replace(old, new)
    return t

for f in SRC.glob("*.css"):
    out_name = f.name.replace("rayquaza", "helcurt").replace("rq35", "helc")
    content = f.read_text("utf-8")
    new_content = transform_css(content)
    (DST / out_name).write_text(new_content, encoding="utf-8")
    print("Built widget:", out_name, len(new_content), "bytes")
print("All widgets built!")
