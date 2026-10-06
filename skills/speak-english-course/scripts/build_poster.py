#!/usr/bin/env python3
"""Render a 1080x1620 WhatsApp poster from an HTML source file.

Usage:  python build_poster.py input.html output.png
"""
import subprocess
import sys
import tempfile
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)

    src, dest = Path(sys.argv[1]), Path(sys.argv[2])
    dest.parent.mkdir(parents=True, exist_ok=True)

    from weasyprint import HTML

    with tempfile.TemporaryDirectory() as tmp:
        pdf = Path(tmp) / "poster.pdf"
        HTML(filename=str(src)).write_pdf(str(pdf))
        stem = Path(tmp) / "page"
        subprocess.run(
            ["pdftoppm", "-png", "-r", "96", "-f", "1", "-l", "1",
             str(pdf), str(stem)],
            check=True,
        )
        rendered = next(Path(tmp).glob("page-*.png"))
        dest.write_bytes(rendered.read_bytes())

    from PIL import Image

    print(f"{dest}  —  {Image.open(dest).size}")


if __name__ == "__main__":
    main()
