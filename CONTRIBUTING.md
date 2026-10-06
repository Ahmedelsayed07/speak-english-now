# Contributing

Fixes to the build scripts, the skill instructions, or the documented
WeasyPrint workarounds are welcome. Open an issue first for anything that
changes the skill's structure.

Course content is not maintained here, so please don't open PRs adding
lessons or units.

## Conventions
- File names: lowercase, hyphenated, ASCII only. `sample-unit.html`, not
  `الوحدة ٥.html` — Arabic in file names breaks on some platforms and shells.
  The Arabic lives inside the files.
- Verify the pipeline still runs before committing a script change:
  `python skills/speak-english-course/scripts/build_pdf.py examples/sample-unit.html output/test.pdf`
- If the course structure changes, update
  `skills/speak-english-course/references/course-map.md` in the same commit.
- CI validates every `SKILL.md`. Run it locally with `python docs/validate_skill.py`.
