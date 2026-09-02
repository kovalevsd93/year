# -*- coding: utf-8 -*-
import build, data, inline, re

# swap remote assets for inlined ones inside the generated markup
LOGOF_D = inline.asset(data.LOGO_FOOT, 96, keep_alpha=True)
PAY_D   = [inline.asset(u, 200, keep_alpha=True) for u in data.PAY_LOGOS]
INST_D  = [inline.asset(u, 200, keep_alpha=True) for u in data.INST_LOGOS]

FONTS = {k: inline.datauri(inline.fetch(v)) for k, v in data.GILROY.items()}
html = build.with_fonts(build.render(inline=inline.review, shots=inline.local_shots), FONTS)
html = html.replace(data.LOGO_FOOT, LOGOF_D)
for u, d in zip(data.PAY_LOGOS, PAY_D):  html = html.replace(u, d)
for u, d in zip(data.INST_LOGOS, INST_D): html = html.replace(u, d)

html = html.replace("{HERO_CARD}", build.hero_card_uri())
assert "tildacdn" not in html, "remote asset left: " + re.search(r'https://\S*tildacdn\S{0,60}', html).group(0)
open("preview.html", "w", encoding="utf-8").write(html)
print("preview.html", round(len(html.encode())/1e6, 2), "MB")
