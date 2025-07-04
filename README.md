# Problem Set Generator

`ps-generator` collects weekly problem sets and their companion mini web apps. Each
`problem-set-N` directory is self-contained so that it can be distributed or
archived independently. The repository currently focuses on static HTML quizzes
backed by JSON question banks, with a roadmap toward automated PDF generation.

## 1 · Purpose

* **Audience** – Students in an introductory probability and data analysis course.
* **Outputs** – A browser-based quiz for immediate feedback and PDFs for offline reference.

## 2 · Repository Layout

| Item                  | Description                                                                           |
|-----------------------|---------------------------------------------------------------------------------------|
| `problem-set-1/`      | Complete unit with slides, a `question_bank.json`, and a deployed web quiz.           |
| `problem-set-2/`      | Second full unit following the same structure.                                        |
| `problem-set-3/`      | In-progress content: blueprint of 20 MCQs and validation utilities.                   |
| `doc/`                | Internal documentation (`audit_ps1_ps2.md`, `schema.md`).                             |
| `tools/`              | Helper scripts such as `extract_questions.py`.                                        |
| `tests/`              | Unit tests ensuring JSON files parse correctly and validate generated TeX.                                       |
| `Refactor_Roadmap.md` | Milestone plan for moving from the prototype to a full generator pipeline.           |
| `LICENSE`             | MIT license covering all source files.                                                |

> Every problem-set directory contains its own `web_app/`, `lecture-slides/`,
> and optional `question_bank.json`. The isolation keeps semester-to-semester
> updates localised.

## 3 · Current Problem Sets

* **Problem Set 1** – 14 MCQs on basic probability. Slides for week 2 are
  included under `lecture-slides/`.
* **Problem Set 2** – 21 MCQs introducing inference for one proportion.
* **Problem Set 3** – Draft blueprint with computation checks; the web quiz is
  not yet finalised.

Extract a fresh JSON bank from any quiz HTML using:

```bash
python tools/extract_questions.py problem-set-N/web_app/index.html \
    problem-set-N/question_bank.json
```

Replace `N` with the desired week number.

## 4 · Development

Run the unit tests whenever question banks change:

```bash
pytest -q
```

HTML can be validated with `tidy` and formatted with `prettier` if available.

Generate TeX versions of a problem set using the CLI:

```bash
python -m generator.build_ps --bank problem-set-N/question_bank.json --out build/
```

You can also compile the resulting TeX into PDFs in one step:

```bash
python -m generator.build_pdf --bank problem-set-N/question_bank.json --out build/
```

## 5 · Roadmap

`Refactor_Roadmap.md` describes the planned evolution of the project. Upcoming
milestones include loading question banks at runtime, generating LaTeX PDFs from
Jinja templates, and improving accessibility across the web apps.
