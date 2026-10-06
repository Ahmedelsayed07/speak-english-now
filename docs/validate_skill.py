#!/usr/bin/env python3
"""Check that every SKILL.md has valid frontmatter with name and description."""
import sys
from pathlib import Path

import yaml

FAILED = False

for skill in sorted(Path("skills").glob("*/SKILL.md")):
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---"):
        print(f"FAIL {skill}: no YAML frontmatter")
        FAILED = True
        continue
    raw = text.split("---", 2)[1]
    try:
        meta = yaml.safe_load(raw) or {}
    except yaml.YAMLError as exc:
        print(f"FAIL {skill}: invalid YAML — {exc}")
        FAILED = True
        continue
    for field in ("name", "description"):
        if not meta.get(field):
            print(f"FAIL {skill}: missing '{field}'")
            FAILED = True
    if meta.get("name") and meta["name"] != skill.parent.name:
        print(f"FAIL {skill}: name '{meta['name']}' != folder '{skill.parent.name}'")
        FAILED = True
    if not FAILED:
        print(f"ok   {skill}")

sys.exit(1 if FAILED else 0)
