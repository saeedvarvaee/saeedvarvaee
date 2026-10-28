#!/usr/bin/env python3
from pathlib import Path
import xml.etree.ElementTree as ET
import re, sys

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

errors=[]
svgs=list(ASSETS.rglob("*.svg"))
for p in svgs:
    try:
        ET.parse(p)
    except Exception as e:
        errors.append(f"{p}: invalid XML: {e}")
    text=p.read_text(encoding="utf-8")
    ids=re.findall(r'\bid="([^"]+)"', text)
    dup=sorted({x for x in ids if ids.count(x)>1})
    if dup:
        errors.append(f"{p}: duplicate ids: {dup}")
    if "<script" in text.lower() or "javascript:" in text.lower():
        errors.append(f"{p}: script/javascript found")
    if "<svg" in text and "viewBox=" not in text:
        errors.append(f"{p}: missing viewBox")
    if "<title" not in text or "<desc" not in text:
        errors.append(f"{p}: missing accessibility title/description")

readme=(ROOT/"README.md").read_text(encoding="utf-8")
refs = re.findall(r'\]\(([^)]+)\)', readme)
refs += re.findall(r'<img[^>]+src="([^"]+)"', readme)
for ref in refs:
    if ref.startswith("./"):
        target=ROOT/ref[2:]
        if not target.exists():
            errors.append(f"README: missing local asset {ref}")

gifs=list((ASSETS / "animations").rglob("*.gif"))
for p in gifs:
    try:
        data=p.read_bytes()
        if not data.startswith((b"GIF87a", b"GIF89a")):
            raise ValueError("missing GIF87a/GIF89a header")
        if len(data) < 10:
            raise ValueError("truncated GIF")
        width=int.from_bytes(data[6:8], "little")
        height=int.from_bytes(data[8:10], "little")
        # Count image descriptors (0x2C); this is sufficient for a lightweight
        # structural check without requiring Pillow or another external package.
        frames=data.count(b"\x2c")
        if frames < 2:
            errors.append(f"{p}: GIF has fewer than 2 image frames")
        if width > 1600:
            errors.append(f"{p}: GIF width exceeds 1600px")
        if p.stat().st_size > 10 * 1024 * 1024:
            errors.append(f"{p}: GIF exceeds 10MB")
    except Exception as e:
        errors.append(f"{p}: invalid GIF: {e}")

required=[
"nexus-hero.svg","financial-orbit.svg","skill-matrix.svg","banking-network.svg",
"career-trajectory.svg","finovaan-network.svg","nexus-divider.svg","profile-signature.svg",
"financial-quote.svg","nexus-404.svg"
]
for name in required:
    if not (ASSETS/name).exists():
        errors.append(f"missing required asset: {name}")

if errors:
    print("VALIDATION FAILED")
    print("\n".join(f"- {x}" for x in errors))
    sys.exit(1)
print(f"PASS: {len(svgs)} SVG files validated; README local references resolved.")
