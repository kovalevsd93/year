# -*- coding: utf-8 -*-
"""Key a flat studio backdrop out of a shot and write an RGBA cut-out.
   Floods inward from the frame edges so enclosed areas survive, then
   feathers the boundary and lifts the backdrop colour back out of it."""
import png, sys
from collections import deque

SRC, DST = sys.argv[1], sys.argv[2]
BG_MIN  = int(sys.argv[3]) if len(sys.argv) > 3 else 253   # backdrop is at least this bright
BG_VAL  = int(sys.argv[4]) if len(sys.argv) > 4 else 254   # its actual value, for un-matting

w, h, d = png.read(SRC)
lum = bytearray(w * h)
for i in range(w * h):
    j = i * 4
    lum[i] = (d[j] * 299 + d[j+1] * 587 + d[j+2] * 114) // 1000

bg = bytearray(w * h)
q = deque()
def seed(i):
    if not bg[i] and lum[i] >= BG_MIN:
        bg[i] = 1; q.append(i)
for x in range(w):
    seed(x); seed((h-1) * w + x)
for y in range(h):
    seed(y * w); seed(y * w + w - 1)
while q:
    i = q.popleft()
    x, y = i % w, i // w
    for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
        if 0 <= nx < w and 0 <= ny < h:
            n = ny * w + nx
            if not bg[n] and lum[n] >= BG_MIN:
                bg[n] = 1; q.append(n)

# drop specks, then feather
alpha = bytearray(w * h)
for y in range(h):
    y0, y1 = max(0, y-1), min(h-1, y+1)
    for x in range(w):
        x0, x1 = max(0, x-1), min(w-1, x+1)
        s = n = 0
        for yy in range(y0, y1+1):
            b = yy * w
            for xx in range(x0, x1+1):
                s += 0 if bg[b+xx] else 1; n += 1
        alpha[y*w+x] = (s * 255) // n

seen = bytearray(w * h); comps = []
for s0 in range(w * h):
    if seen[s0] or alpha[s0] <= 24: continue
    qq = deque([s0]); seen[s0] = 1; cells = []
    while qq:
        i = qq.popleft(); cells.append(i)
        x, y = i % w, i // w
        for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if 0 <= nx < w and 0 <= ny < h:
                n = ny * w + nx
                if not seen[n] and alpha[n] > 24:
                    seen[n] = 1; qq.append(n)
    comps.append(cells)
comps.sort(key=len, reverse=True)
keep = set()
for c in comps:
    if len(c) >= 3000: keep.update(c)
print('components kept:', sum(1 for c in comps if len(c) >= 3000),
      'largest:', [len(c) for c in comps[:3]])
for i in range(w * h):
    if i not in keep: alpha[i] = 0

out = bytearray(w * h * 4)
xs0, ys0, xs1, ys1 = w, h, 0, 0
for i in range(w * h):
    a = alpha[i]; j = i * 4
    if a == 0:
        out[j:j+4] = b"\xff\xff\xff\x00"; continue
    if a < 255:
        f = a / 255.0
        for c in range(3):
            v = (d[j+c] - BG_VAL * (1 - f)) / f
            out[j+c] = 0 if v < 0 else (255 if v > 255 else int(v))
    else:
        out[j:j+3] = d[j:j+3]
    out[j+3] = a
    x, y = i % w, i // w
    if x < xs0: xs0 = x
    if x > xs1: xs1 = x
    if y < ys0: ys0 = y
    if y > ys1: ys1 = y

pad = 3
xs0, ys0 = max(0, xs0-pad), max(0, ys0-pad)
xs1, ys1 = min(w-1, xs1+pad), min(h-1, ys1+pad)
nw, nh = xs1-xs0+1, ys1-ys0+1
crop = bytearray(nw * nh * 4)
for y in range(nh):
    s = ((y+ys0) * w + xs0) * 4
    crop[y*nw*4:(y+1)*nw*4] = out[s:s+nw*4]
png.write(DST, nw, nh, crop)
print(f'wrote {DST}  {nw}x{nh}')
