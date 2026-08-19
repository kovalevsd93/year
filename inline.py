# -*- coding: utf-8 -*-
import os, base64, subprocess, hashlib, urllib.request, mimetypes
from data import CDN
CACHE = "cache"
os.makedirs(CACHE, exist_ok=True)

def fetch(url):
    h = hashlib.md5(url.encode()).hexdigest()[:16]
    ext = os.path.splitext(url)[1].lower() or ".bin"
    p = os.path.join(CACHE, h + ext)
    if not os.path.exists(p):
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r, open(p, "wb") as f:
            f.write(r.read())
    return p

def shrink(path, width, quality=58):
    out = path + f".w{width}.jpg"
    if not os.path.exists(out):
        subprocess.run(["sips", "-Z", str(width), path, "--out", out,
                        "-s", "format", "jpeg", "-s", "formatOptions", str(quality)],
                       check=True, capture_output=True)
    return out

def shrink_png(path, width):
    out = path + f".w{width}.png"
    if not os.path.exists(out):
        subprocess.run(["sips", "-Z", str(width), path, "--out", out],
                       check=True, capture_output=True)
    return out

def datauri(path):
    mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
    return "data:%s;base64,%s" % (mime, base64.b64encode(open(path, "rb").read()).decode())

def review(rel):
    return datauri(shrink(fetch(CDN + rel), 520, 55))

def asset(url, width=None, keep_alpha=False):
    p = fetch(url)
    if url.endswith(".svg"):
        return datauri(p)
    if width:
        p = shrink_png(p, width) if keep_alpha else shrink(p, width, 72)
    return datauri(p)


def local_shots(folder, width=760, quality=62):
    """Every image in `folder`, downscaled and inlined. Empty list if absent."""
    import glob
    out = []
    if not os.path.isdir(folder):
        return out
    files = sorted(f for f in glob.glob(os.path.join(folder, "*"))
                   if os.path.splitext(f)[1].lower() in
                   (".png", ".jpg", ".jpeg", ".webp", ".heic"))
    for f in files:
        dst = os.path.join(CACHE, "shot_" + hashlib.md5(f.encode()).hexdigest()[:12]
                           + f".w{width}.jpg")
        if not os.path.exists(dst):
            r = subprocess.run(["sips", "-Z", str(width), f, "--out", dst,
                                "-s", "format", "jpeg", "-s", "formatOptions", str(quality)],
                               capture_output=True)
            if r.returncode != 0 or not os.path.exists(dst):
                print(f"  ! пропустил {os.path.basename(f)}: sips не смог открыть")
                continue
        out.append((datauri(dst), dst))
    return out
