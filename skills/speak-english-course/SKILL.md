---
name: speak-english-course
description: >
  Produces daily lessons, tasks, WhatsApp messages, voice-note scripts, poster
  images, session run-sheets and unit PDFs for "Speak English Now" — a 30-day
  Arabic-language English speaking course for Egyptian learners, taught through
  WhatsApp with the mascots Abqour El-Shatour (A0–A2) and Mr. Nori (B1–C1).
  Use this skill whenever the user asks for course content in Egyptian Arabic:
  a daily lesson or task, a voice-note script, a lesson/task poster, a unit PDF,
  a live-session agenda, a group announcement, a reply to a student, or any
  sales/marketing copy for the course. Also use it when the user names a day
  number ("day 16"), a unit number ("unit 6"), or either mascot by name.
license: MIT
---

# Speak English Now — Course Production Skill

Produce course material that is indistinguishable from the existing 30 days of
output. Match the voice, the structure, and the constraints exactly.

## Before producing anything

1. Read `references/voice-and-tone.md` — the writing rules. Non-negotiable.
2. Read `references/course-map.md` — what day/unit covers what.
3. For a PDF, read `references/pdf-pipeline.md` and use `assets/style.css`.
4. For a poster, read `references/poster-spec.md`.

## Where content lives

This repository contains the *system*, not the course text. The actual units,
lessons and posters live in a private `content/` folder that is git-ignored.
When generating material, write new files to `content/` (create it if absent)
and build outputs into `output/`.

## What this skill produces

| Request | Deliverable | Reference |
|---|---|---|
| "درس اليوم X" | WhatsApp message + 3-min voice script | `course-map.md` |
| "تاسك اليوم X" | WhatsApp task message + optional AI prompt | `course-map.md` |
| "poster" / "صورة" | 1080×1620 PNG via HTML→PDF→PNG | `poster-spec.md` |
| "الوحدة X PDF" | A4 RTL PDF, 10–15 pages | `pdf-pipeline.md` |
| "سيشن" / "session" | Presenter run-sheet PDF, timed by the minute | `pdf-pipeline.md` |
| "رد على الطالب" | A reply in the course's voice | `voice-and-tone.md` |

## Hard constraints

- **Egyptian Arabic**, not Modern Standard Arabic. Write as the trainer speaks.
- **No em dashes** (`—`) as a sentence device in Arabic prose. They read as AI.
- WhatsApp formatting uses `*bold*` and `_italic_` — never Markdown `**`.
- Every lesson ends with a task. Every task has a 9 PM deadline.
- Every task requires a **voice note**, unless the day is explicitly an AI day
  or a rest day.
- Never promise fluency. Promise a specific, checkable outcome.
- English example sentences must be A2–B1 for Abqour, B2–C1 for Mr. Nori.
  Never upgrade a learner's vocabulary beyond their level.

## Two mascots, two brands

| | Abqour El-Shatour | Mr. Nori |
|---|---|---|
| Level | A0 → A2 | B1 → C1 |
| Tone | Warm, encouraging, playful | Sharp, professional, confident |
| Palette | Navy `#0B2F77`, gold `#FFD166`, beige `#F6DAC1` | Black `#0A0A0A`, matrix green `#2BFF7A`, light `#F1F4F1` |
| Asset | `assets/abqour.png` | `assets/nori.png` |

## Workflow for a daily post

1. Identify the day number and its unit from `references/course-map.md`.
2. Draft the WhatsApp lesson message (sections separated by `━━━`).
3. Draft the voice-note script with **timestamps and pause markers** — the
   pauses are where learners repeat. Never omit them.
4. Draft the task message with conditions and the 9 PM deadline.
5. Only build a poster if asked, or if the content is a comparison/list that
   reads better visually.

## Verification before delivering

- Count any number you state in prose against the list you actually wrote.
- Read the Arabic aloud. If a sentence sounds written rather than spoken,
  rewrite it.
- Check the English level matches the mascot.
- Confirm the task is doable in under 60 seconds of speech.
