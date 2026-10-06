# Poster Spec

WhatsApp posters are **1080 × 1620 px** (2:3). Built as HTML, rendered through
WeasyPrint at a custom page size, then rasterised.

```css
@page { size: 1080px 1620px; margin: 0 }
```
```bash
python scripts/build_poster.py content/posters/day-15.html output/day-15.png
```

## Fixed anatomy
| Zone | Height | Contents |
|---|---|---|
| Header | ~150px | day label, title, subtitle, gold bottom border |
| Mascot row | ~340px | mascot bottom-left, speech bubble right |
| Body | flexible | 2–5 cards |
| Footer | ~110px | deadline + credit line |

## Rules
- The speech bubble carries **the hook**, not a summary.
- Maximum five body blocks. More than that and nobody reads it.
- English goes in `direction: ltr; unicode-bidi: isolate`.
- Never put a copy-paste prompt in an image. Prompts go in the text message so
  learners can actually copy them.
- Red is reserved for traps and errors. Green for correct forms.
