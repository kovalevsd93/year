# -*- coding: utf-8 -*-
"""Интринсик-размеры картинок, чтобы браузер резервировал под них место
   и страница не переверстывалась по мере загрузки."""
import json, os, subprocess, hashlib, urllib.request

STORE = "dims.json"
CACHE = "cache"
_db = json.load(open(STORE)) if os.path.exists(STORE) else {}
_dirty = False

def _measure(path):
    r = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", path],
                       capture_output=True, text=True)
    w = h = None
    for line in r.stdout.splitlines():
        if "pixelWidth:" in line:  w = int(line.split(":")[1])
        if "pixelHeight:" in line: h = int(line.split(":")[1])
    return (w, h) if w and h else None

def of(src):
    """src — путь на диске или http(s)-адрес. Возвращает (w, h) или None."""
    global _dirty
    if src in _db:
        return tuple(_db[src]) if _db[src] else None
    size = None
    try:
        if src.startswith("http"):
            os.makedirs(CACHE, exist_ok=True)
            p = os.path.join(CACHE, "dim_" + hashlib.md5(src.encode()).hexdigest()[:16]
                             + os.path.splitext(src)[1][:5])
            if not os.path.exists(p):
                req = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=60) as r, open(p, "wb") as f:
                    f.write(r.read())
            size = _measure(p)
        elif os.path.exists(src):
            size = _measure(src)
    except Exception:
        size = None
    _db[src] = list(size) if size else None
    _dirty = True
    return size

def attrs(src):
    s = of(src)
    return f' width="{s[0]}" height="{s[1]}"' if s else ""

def save():
    if _dirty:
        json.dump(_db, open(STORE, "w"), indent=0)
