# Speak English Now

A 30-day spoken-English course for Arabic speakers, taught through WhatsApp.
Built and run by **Ahmed Elsayed**.

Two tracks, two mascots:

| Track | Level | Mascot | Focus |
|---|---|---|---|
| **Speak English Now** | A0 → A2 | Abqour El-Shatour 🐥 | Pronunciation, self-introduction, interviews |
| **Speak English Pro** | B1 → C1 | Mr. Nori | Meetings, presentations, negotiation, business writing |

## Results — cohort 01

| Metric | Value |
|---|---|
| Enrolled | 550 |
| Completed the 30 days | 250 (45%) |
| Used English in a real situation | 170 (68% of finishers) |

Full write-up in [`docs/case-study.md`](docs/case-study.md).

## Repository layout

```
.
├── skills/
│   └── speak-english-course/     Agent Skill — generates course material
│       ├── SKILL.md
│       ├── references/           voice, course map, build pipelines
│       ├── scripts/              PDF and poster builders
│       └── assets/               brand CSS + mascot images
├── examples/                     one stripped-down source file to build against
├── brand/                        palette, fonts, sizes
├── docs/                         case study, how to run a cohort
└── output/                       built files (git-ignored)
```

> **The course content is not in this repository.** Lessons, tasks, unit PDFs
> and poster sources are licensed material for enrolled cohorts. What is here
> is the *system* that produces them: the skill, the build pipeline, the brand,
> and the methodology. `content/` is git-ignored — keep your own units there
> locally or in a private repo.


## Using the Agent Skill

**Claude Code** — clone and symlink:
```bash
git clone https://github.com/Ahmedelsayed07/speak-english-now.git
ln -s "$PWD/speak-english-now/skills/speak-english-course" ~/.claude/skills/
```

**claude.ai** — zip the skill folder and upload under
Settings → Capabilities → Skills:
```bash
cd skills && zip -r speak-english-course.zip speak-english-course
```

Then ask for what you need:

> درس اليوم ١٦ وتاسكه
> اعملي بوستر للوحدة ٦
> أجندة سيشن ٩٠ دقيقة لمجموعة ٥٠

## Building a PDF

```bash
pip install weasyprint pypdf pillow --break-system-packages
sudo apt-get install -y fonts-noto-core          # Arabic shaping
python skills/speak-english-course/scripts/build_pdf.py \
       examples/sample-unit.html output/sample-unit.pdf
```

## Licence

Code, build scripts and templates: [MIT](LICENSE).

Course text, lesson scripts, mascot artwork and brand: **all rights reserved**.
See [`LICENSE-CONTENT`](LICENSE-CONTENT). The mascots *Abqour El-Shatour* and
*Mr. Nori* may not be reused.
