# -*- coding: utf-8 -*-
def _s(p, c="#6558BC", w="1.6"):
    return ('<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="%s" '
            'stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>') % (c, w, p)

ICONS = {
 "heart": '<path d="M12 20s-7-4.35-7-9a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 4.65-7 9-7 9Z"/>',
 "body":  '<circle cx="12" cy="5" r="2.4"/><path d="M12 7.6v7M12 14.6 8.6 20M12 14.6 15.4 20M7.5 10.5h9"/>',
 "mind":  '<path d="M15.5 19.5a4 4 0 0 0 3.2-6.4A4.2 4.2 0 0 0 16.4 6a4.4 4.4 0 0 0-8.6.7A4 4 0 0 0 6.4 14a4 4 0 0 0 3.4 5.5"/><path d="M12 7v13"/>',
 "steps": '<path d="M4 19h4v-4h4v-4h4V7h4"/>',
 "leaf":  '<path d="M5 19C4 12 8.5 6.5 19 5.5 19.5 15 14 19.5 7 19"/><path d="M5 19c2.5-3.5 5.5-6 9.5-8"/>',
 "clock": '<circle cx="12" cy="12" r="8"/><path d="M12 7.5V12l3 1.8"/>',
 "people":'<circle cx="9" cy="9" r="2.8"/><path d="M3.8 19a5.4 5.4 0 0 1 10.4 0"/><path d="M16 6.4a2.8 2.8 0 0 1 0 5.4M17.4 14.4A5.4 5.4 0 0 1 20.5 19"/>',
 "live":  '<rect x="3" y="5.5" width="14" height="13" rx="3"/><path d="M17 11.2l4-2.4v6.4l-4-2.4z"/>',
 "spark": '<path d="M12 4l1.7 4.6L18.5 10l-4.8 1.4L12 16l-1.7-4.6L5.5 10l4.8-1.4L12 4Z"/><path d="M18 16.5l.8 2 2 .8-2 .8-.8 2-.8-2-2-.8 2-.8.8-2Z"/>',
 "compass":'<circle cx="12" cy="12" r="8.2"/><path d="M14.8 9.2l-1.6 4.2-4.2 1.6 1.6-4.2 4.2-1.6Z"/>',
 "shield":'<path d="M12 3.5 19 6v5.2c0 4.2-2.9 7.5-7 9.3-4.1-1.8-7-5.1-7-9.3V6l7-2.5Z"/>',
 "users": '<circle cx="12" cy="8" r="3"/><path d="M5.5 19.5a6.5 6.5 0 0 1 13 0"/>',
 "calendar":'<rect x="4" y="5.5" width="16" height="14" rx="3"/><path d="M4 10h16M9 3.5v4M15 3.5v4"/>',
}
def icon(name, color="#6558BC"):
    return _s(ICONS[name], color)

# one mark per condition — the thing it actually feels like, not a generic symbol
COND = {
 # a burst: the spike that arrives out of nowhere
 "panic":  '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8'
           'M18.4 5.6l-2.8 2.8M8.4 15.6l-2.8 2.8"/><circle cx="12" cy="12" r="3"/>',
 # a spiral: dizziness, the ground tilting
 "vsd":    '<path d="M12 12a2.2 2.2 0 1 1 2.2 2.2A4.4 4.4 0 0 1 9.8 9.8'
           'A6.6 6.6 0 0 1 16.4 3.2 8.8 8.8 0 0 1 21 12a9 9 0 1 1-9-9"/>',
 # a low wave that never resolves: the background hum
 "gad":    '<path d="M2 14c1.7 0 1.7-4 3.3-4S7 14 8.7 14s1.6-4 3.3-4 1.7 4 3.3 4 1.7-4 3.4-4'
           'S20.3 14 22 14"/>',
 # a magnifier over the body: scanning yourself for damage
 "health": '<circle cx="10.5" cy="10.5" r="6"/><path d="M15 15l5.5 5.5"/>'
           '<path d="M10.5 8v5M8 10.5h5"/>',
 # a doorway you stop in front of
 "agora":  '<path d="M4 20V5a1 1 0 0 1 1-1h9a1 1 0 0 1 1 1v15"/><path d="M2.5 20h14"/>'
           '<path d="M12 12.2h.01"/><path d="M19 8v8M19 16l-2.4-2.4M19 16l2.4-2.4"/>',
 # a closed loop you keep going round
 "ocd":    '<path d="M20 12a8 8 0 1 1-3.3-6.5"/><path d="M20.5 3.5V9h-5.5"/>'
           '<circle cx="12" cy="12" r="2.4"/>',
 # a heart you keep listening to
 "cardio": '<path d="M12 20s-7.5-4.7-7.5-9.8A4.3 4.3 0 0 1 12 7a4.3 4.3 0 0 1 7.5 3.2'
           'c0 1.1-.35 2.15-.9 3.1"/><path d="M3 13.4h4l1.6-2.8 2.2 5 1.7-3.4 1.1 1.9h5.9"/>',
}
def cond_icon(name, color, size=26):
    return ('<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="%s" '
            'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true">%s</svg>') % (size, size, color, COND[name])

ICONS.update({
 "map":    '<path d="M9 5.2 3.5 7.4v11.4L9 16.6l6 2.6 5.5-2.2V5.6L15 7.8Z"/>'
           '<path d="M9 5.2v11.4M15 7.8v11.4"/>',
 "note":   '<path d="M19 13.5V19a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h5.4"/>'
           '<path d="M17.4 3.6a1.9 1.9 0 0 1 2.7 2.7L13 13.4l-3.2.9.9-3.2Z"/>',
 "layers": '<path d="M12 3.6 3.6 8 12 12.4 20.4 8Z"/><path d="M3.6 12.4 12 16.8l8.4-4.4"/>'
           '<path d="M3.6 16.6 12 21l8.4-4.4"/>',
 "ear":    '<path d="M4 11a8 8 0 0 1 16 0v5.5a3.5 3.5 0 0 1-6.4 2"/>'
           '<path d="M4 14.5v-2M20 14.5v-2"/><path d="M8.5 11a3.5 3.5 0 1 1 7 0c0 2.2-2.6 2.6-2.6 5"/>',
 "letter": '<rect x="3.2" y="5.4" width="17.6" height="13.2" rx="2.6"/>'
           '<path d="m4.4 7 6.3 4.9a2 2 0 0 0 2.6 0L19.6 7"/>',
 "target": '<circle cx="12" cy="12" r="8.2"/><circle cx="12" cy="12" r="4.2"/>'
           '<circle cx="12" cy="12" r="1"/>',
})

def any_icon(name, color, size=22):
    """COND marks first, then the general set."""
    if name in COND:
        return cond_icon(name, color, size)
    return _s(ICONS[name], color)

ICONS["check"] = '<path d="M20 6L9 17l-5-5"/>'

def marker_uri(name, color, width="2"):
    """Any mark as a CSS url() — percent-encoded so it can live in a style attribute."""
    from urllib.parse import quote
    path = COND.get(name) or ICONS[name]
    svg = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' "
           f"stroke='{color}' stroke-width='{width}' stroke-linecap='round' "
           f"stroke-linejoin='round'>{path}</svg>")
    return "url(data:image/svg+xml," + quote(svg, safe="") + ")"
