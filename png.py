# -*- coding: utf-8 -*-
"""Minimal PNG read/write (8-bit, non-interlaced) — no third-party deps."""
import zlib, struct

def _paeth(a, b, c):
    p = a + b - c
    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
    if pa <= pb and pa <= pc: return a
    if pb <= pc: return b
    return c

def read(path):
    raw = open(path, "rb").read()
    assert raw[:8] == b"\x89PNG\r\n\x1a\n", "not a png"
    pos, idat, pal, trns = 8, [], None, None
    while pos < len(raw):
        ln = struct.unpack(">I", raw[pos:pos+4])[0]
        typ = raw[pos+4:pos+8]
        data = raw[pos+8:pos+8+ln]
        if typ == b"IHDR":
            w, h, depth, ctype, comp, filt, inter = struct.unpack(">IIBBBBB", data)
            assert depth == 8 and inter == 0, f"unsupported png (depth {depth}, interlace {inter})"
        elif typ == b"PLTE": pal = data
        elif typ == b"tRNS": trns = data
        elif typ == b"IDAT": idat.append(data)
        elif typ == b"IEND": break
        pos += 12 + ln
    ch = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[ctype]
    buf = bytearray(zlib.decompress(b"".join(idat)))
    stride = w * ch
    out = bytearray(h * stride)
    prev = bytearray(stride)
    p = 0
    for y in range(h):
        f = buf[p]; p += 1
        line = bytearray(buf[p:p+stride]); p += stride
        if f == 1:
            for i in range(ch, stride): line[i] = (line[i] + line[i-ch]) & 255
        elif f == 2:
            for i in range(stride): line[i] = (line[i] + prev[i]) & 255
        elif f == 3:
            for i in range(stride):
                a = line[i-ch] if i >= ch else 0
                line[i] = (line[i] + ((a + prev[i]) >> 1)) & 255
        elif f == 4:
            for i in range(stride):
                a = line[i-ch] if i >= ch else 0
                c = prev[i-ch] if i >= ch else 0
                line[i] = (line[i] + _paeth(a, prev[i], c)) & 255
        out[y*stride:(y+1)*stride] = line
        prev = line

    # normalise everything to RGBA
    rgba = bytearray(w * h * 4)
    for i in range(w * h):
        if ctype == 6:
            rgba[i*4:i*4+4] = out[i*4:i*4+4]
        elif ctype == 2:
            rgba[i*4:i*4+3] = out[i*3:i*3+3]; rgba[i*4+3] = 255
        elif ctype == 0:
            g = out[i]; rgba[i*4:i*4+3] = bytes((g, g, g)); rgba[i*4+3] = 255
        elif ctype == 4:
            g, a = out[i*2], out[i*2+1]
            rgba[i*4:i*4+3] = bytes((g, g, g)); rgba[i*4+3] = a
        elif ctype == 3:
            idx = out[i]
            rgba[i*4:i*4+3] = pal[idx*3:idx*3+3]
            rgba[i*4+3] = trns[idx] if trns and idx < len(trns) else 255
    return w, h, rgba

def write(path, w, h, rgba, level=9):
    lines = bytearray()
    stride = w * 4
    for y in range(h):
        lines.append(0)
        lines += rgba[y*stride:(y+1)*stride]
    def chunk(typ, data):
        return (struct.pack(">I", len(data)) + typ + data
                + struct.pack(">I", zlib.crc32(typ + data) & 0xffffffff))
    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(bytes(lines), level))
           + chunk(b"IEND", b""))
    open(path, "wb").write(png)
