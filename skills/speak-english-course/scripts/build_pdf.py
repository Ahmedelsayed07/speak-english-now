#!/usr/bin/env python3
"""Build an Arabic RTL PDF from an HTML source file.

Usage:  python build_pdf.py input.html output.pdf

Applies the three WeasyPrint fixes documented in references/pdf-pipeline.md:
explicit column widths, separate borders, and bidi punctuation repair.
"""
import re
import sys
from pathlib import Path


def add_colgroups(html: str) -> str:
    """Give every table an explicit <colgroup>.

    WeasyPrint assigns mixed percentage/auto column widths in reverse order,
    so every column needs a stated width.
    """
    def fix(match: re.Match) -> str:
        table = match.group(0)
        if "<colgroup" in table:
            return table
        header = re.search(r"<tr>(?:(?!</tr>).)*?<th\b.*?</tr>", table, re.S)
        if not header:
            return table
        cells = re.findall(r"<th\b[^>]*>", header.group(0))
        if not cells:
            return table
        widths = []
        for cell in cells:
            found = re.search(r"width:\s*([\d.]+)%", cell)
            widths.append(found.group(1) if found else None)
        known = sum(float(w) for w in widths if w)
        missing = [i for i, w in enumerate(widths) if w is None]
        if missing:
            each = round(max(100 - known, len(missing) * 5) / len(missing), 2)
            widths = [w if w else str(each) for w in widths]
        cols = "".join(f'<col style="width:{w}%">' for w in widths)
        table = re.sub(r"(<th\b[^>]*?)width:\s*[\d.]+%;?\s*", r"\1", table)
        table = table.replace('<th style="">', "<th>")
        return re.sub(r"(<table[^>]*>)", r"\1<colgroup>" + cols + "</colgroup>",
                      table, count=1)

    return re.sub(r"<table[^>]*>.*?</table>", fix, html, flags=re.S)


def fix_bidi_punctuation(html: str) -> str:
    """Pull a trailing period inside its LTR span so it doesn't jump the line."""
    return re.sub(r"</span>\.", ".</span>", html)


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)

    src, dest = Path(sys.argv[1]), Path(sys.argv[2])
    html = src.read_text(encoding="utf-8")
    html = fix_bidi_punctuation(add_colgroups(html))

    built = src.with_suffix(".built.html")
    built.write_text(html, encoding="utf-8")

    from weasyprint import HTML  # imported late so --help works without it

    dest.parent.mkdir(parents=True, exist_ok=True)
    HTML(filename=str(built)).write_pdf(str(dest))
    built.unlink()

    from pypdf import PdfReader

    print(f"{dest}  —  {len(PdfReader(str(dest)).pages)} pages")


if __name__ == "__main__":
    main()
