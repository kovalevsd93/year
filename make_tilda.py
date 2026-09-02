# -*- coding: utf-8 -*-
"""Пакует страницу для вставки в Zero Block на Tilda.

В отличие от index.html и preview.html, свои картинки (шапка, логотип,
фото Павла в программе, скриншоты бонуса) здесь НЕ вшиваются base64 — Zero Block
у Tilda отказывается сохранять блок, если в нём слишком много контента.
Вместо этого картинки подгружаются по прямой ссылке с уже опубликованного
GitHub Pages — код остаётся маленьким, а сама картинка остаётся той же.
Шрифты, логотип и скриншоты отзывов и так берутся с CDN самой Tilda
(как и в index.html) — тут ничего менять не нужно.
"""
import base64
import glob
import os
import urllib.parse

import build
import dims

GH_BASE = "https://kovalevsd93.github.io/year"


def gh_shots(folder):
    files = sorted(
        f for f in glob.glob(os.path.join(folder, "*"))
        if os.path.splitext(f)[1].lower() in (".png", ".jpg", ".jpeg", ".webp"))
    return [(GH_BASE + "/" + urllib.parse.quote(f), f) for f in files]


doc = build.with_fonts(build.render(shots=gh_shots), build.GILROY)
doc = doc.replace("{HERO_CARD}", f"{GH_BASE}/assets/hero-card.jpg")

# prog_photo() и logo_uri() вшивают свои картинки как base64 безусловно —
# меняем именно эти строки на ссылки, ничего в build.py не трогая
def _b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()

doc = doc.replace(_b64("assets/pavel-course.png", "image/png"), f"{GH_BASE}/assets/pavel-course.png")
doc = doc.replace(_b64("assets/logo-tree.png", "image/png"), f"{GH_BASE}/assets/logo-tree.png")

lines = doc.split("\n")
assert lines[0].startswith("<meta charset")
assert lines[1].startswith("<meta name=\"viewport\"")
assert lines[2].startswith("<title")
assert lines[3].startswith("<meta name=\"description\"")
# viewport оставляем — без него мобильный Safari в Zero Block рендерит
# страницу как десктопную и потом ужимает картинкой. Title/description
# убираем: это поля настроек страницы в Tilda, а не самого блока.
body = "\n".join([lines[1]] + lines[4:]).lstrip("\n")

import re
leftover = re.findall(r'data:image/(?:jpeg|png)[^"\')]*', body)
assert not leftover, f"осталась незамененная картинка ({len(leftover)} шт.) — Zero Block снова разбухнет"

dims.save()
open("tilda-zeroblock.html", "w", encoding="utf-8").write(body)
print("tilda-zeroblock.html", round(len(body.encode()) / 1e6, 3), "MB")
