"""News-image entry: copy the fixed front-page image to /output/entry.png.

Deterministic: the same bytes on every run. No network, no randomness,
no timestamps, standard library only. Outside the grader's container,
MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1 << 20  # competition cap: 1 MiB

src = HERE / "entry.png"
data = src.read_bytes()
if data[:8] != PNG_SIGNATURE:
    sys.exit("entry.png is not a PNG file")
if len(data) > MAX_BYTES:
    sys.exit("entry.png exceeds the 1 MiB cap")

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, OUT / "entry.png")
if hashlib.sha256((OUT / "entry.png").read_bytes()).hexdigest() != hashlib.sha256(data).hexdigest():
    sys.exit("copied entry.png does not match the source")
