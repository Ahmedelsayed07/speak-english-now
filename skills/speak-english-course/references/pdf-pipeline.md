# PDF Pipeline

Arabic RTL PDFs are built as **HTML → WeasyPrint → PDF**. Do not use reportlab:
it has no Arabic shaping.

## Setup (once per environment)
```bash
pip install weasyprint --break-system-packages
apt-get install -y fonts-noto-core     # Noto Sans Arabic
```
Latin text uses **Carlito**, Arabic falls back to **Noto Sans Arabic**.
Font stack: `'Carlito','Noto Sans Arabic', sans-serif`.

## Build
```bash
python scripts/build_pdf.py content/units/unit-05.html output/unit-05.pdf
```

## Four rules learned the hard way

1. **Tables need explicit widths on every column.** Mixing `width:40%` with
   `auto` makes WeasyPrint assign them in reverse order. `scripts/build_pdf.py`
   injects a `<colgroup>` automatically — keep that step.

2. **Use `border-collapse: separate`.** With `collapse`, a table that splits
   across a page break renders its first fragment with reversed column widths.

3. **Bidi punctuation.** A `.` after an English `<span>` inside RTL text jumps
   to the start of the line. The build script rewrites `</span>.` to `.</span>`.

4. **Watermarks need a transparent body.** Set the page colour on `@page`, not
   on `body`, or the body background paints over the watermark.

## Page anatomy
- Cover: full-bleed, `@page cover { margin: 0 }`
- Content: A4, `margin: 20mm 15mm 18mm`
- Every chapter starts with `.chapter { break-before: page }`
