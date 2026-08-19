# -*- coding: utf-8 -*-
"""The mannequin photograph, with per-zone accent lighting.

The cut-out's own alpha channel is the mask, so the lit area follows the
real silhouette exactly; a radial gradient inside that mask decides which
part of the body is lit. Multiply blending keeps the photo's modelling."""

# gradient geometry measured off the cut-out (447x768), as % of the box
SPOTS = {
 "mind":  ("14% 10%", "47% 8%"),
 "heart": ("18% 11%", "41% 31%"),
 "body":  ("38% 22%", "40% 32%"),
 "steps": ("31% 8%",  "56% 53%"),
}

HOTSPOTS = {"mind": ("47%", "7%"),  "heart": ("41%", "31%"),
            "body": ("14%", "33%"), "steps": ("74%", "54%")}

def spot_css(colors=None):
    """One gradient per zone. `colors` maps zone -> hex, so each level of the
    model is lit in its own colour instead of the single accent."""
    out = []
    for zone, (radii, at) in SPOTS.items():
        c = (colors or {}).get(zone, "#6C5FC0")
        r, g, b = int(c[1:3], 16), int(c[3:5], 16), int(c[5:7], 16)
        out.append(f'.mq-lit[data-zone="{zone}"]{{background:radial-gradient('
                   f'ellipse {radii} at {at},{c} 0%,{c} 42%,'
                   f'rgba({r},{g},{b},0) 100%)}}')
    return "\n".join(out)

def figure(levels):
    lits = "".join(f'<div class="mq-lit" data-zone="{ic}"></div>' for _, ic, _, _ in levels)
    return f'<div class="mq" aria-hidden="true"><div class="mq-base"></div>{lits}</div>'
