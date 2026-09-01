# -*- coding: utf-8 -*-
"""Пакует страницу для вставки в Zero Block на Tilda: тот же код, что в
index.html (картинки Павла/логотипов/отзывов и шрифты — с CDN самой Tilda,
свои картинки — инлайном), только без <meta>/<title> в начале — это
задаётся в настройках страницы Tilda, а не внутри блока."""
import build
import inline as _inline

doc = build.with_fonts(build.render(shots=_inline.local_shots), build.GILROY)
doc = doc.replace("__MANNEQUIN__", build.mannequin_uri())
doc = doc.replace("{HERO_CARD}", build.hero_card_uri())

lines = doc.split("\n")
assert lines[0].startswith("<meta charset")
assert lines[2].startswith("<title")
body = "\n".join(lines[4:]).lstrip("\n")

open("tilda-zeroblock.html", "w", encoding="utf-8").write(body)
print("tilda-zeroblock.html", round(len(body.encode()) / 1e6, 2), "MB")
