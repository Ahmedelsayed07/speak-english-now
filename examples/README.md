# Examples

The course content itself is **not** in this repository — it is licensed
material for enrolled cohorts.

What lives here instead: a single, stripped-down sample that shows the shape
of a source file, so the build scripts and the skill have something to run
against.

```
examples/
└── sample-unit.html      minimal unit source — structure only, no lesson content
```

Build it:

```bash
python skills/speak-english-course/scripts/build_pdf.py \
       examples/sample-unit.html output/sample-unit.pdf
```

If you are running a cohort, keep your real units in a private repository or a
local `content/` folder — `.gitignore` already excludes it.
