Below is a pragmatic **refactor + feature roadmap** that takes the current “all-in-one index.html” prototype and evolves it into a maintainable pipeline with three new artefacts:

* **`question_bank.json`** – single source of truth for questions & answers
* **`generator/build_ps.py`** – CLI that converts the JSON into nicely-typeset PDFs
* **`web_app/script.js`** – runtime logic that loads the same JSON and handles grading

The work is split into four milestones so you can merge early and often.

---

## Milestone 0 · Baseline Audit (½ day)

| Task                         | Detail                                                                        | Deliverable         |
| ---------------------------- | ----------------------------------------------------------------------------- | ------------------- |
| Inventory existing HTML quiz | List every question, choices, and correct answer flag                         | Markdown audit note |
| Decide JSON schema           | `id`, `stem`, `choices:[{text,correct}]`, `explanation`, `tags`, `difficulty` | `doc/schema.md`     |
| Tag each question            | Concept tags (“CLT”, “paired t”, …) & Bloom level                             | Updated audit note  |

*Outcome:* shared understanding of scope before touching code.

---

## Milestone 1 · Extract Question Bank (1 day)

| Task                    | Detail                                                                | Deliverable                            |
| ----------------------- | --------------------------------------------------------------------- | -------------------------------------- |
| Write one-off extractor | Python script uses `BeautifulSoup` to parse `index.html` → list(dict) | `tools/extract_questions.py`           |
| Manual review & polish  | Fill in missing explanations, fix math markup (LaTeX in strings)      | **`problem-set-N/question_bank.json`** |
| Unit test               | Assert counts & sample IDs; pytest in CI                              | `tests/test_questions.py`              |

### JSON Schema (v 1.0)

```jsonc
{
  "lecture": "Week5",
  "questions": [
    {
      "id": "W5-Q01",
      "stem": "What is the pooled estimate of \\(p\\) under H₀?",
      "choices": [
        {"key": "A", "text": "\\(0.25\\)", "correct": false},
        {"key": "B", "text": "\\(0.30\\)", "correct": true},
        {"key": "C", "text": "\\(0.55\\)", "correct": false}
      ],
      "explanation": "The pooled estimate is …",
      "tags": ["two-proportions", "hypothesis-test"],
      "difficulty": "medium"
    }
  ]
}
```

---

## Milestone 2 · Web-App Refactor (1–2 days)

| Task                          | Detail                                                                | Deliverable                           |
| ----------------------------- | --------------------------------------------------------------------- | ------------------------------------- |
| **Script loader**             | `script.js` fetches `question_bank.json` (same directory)             | `/web_app/script.js`                  |
| Render engine                 | Vanilla JS: build DOM from JSON (templated `<fieldset>`)              | Updated `index.html` (now only shell) |
| Grader                        | On submit, iterate questions, compare, show score & per-item feedback | `script.js`                           |
| Accessibility pass            | `<legend>`, `aria-live`, keyboard nav                                 | Tested pages                          |
| Remove duplicated data        | Delete hard-coded radio blocks from `index.html`                      | Clean diff                            |
| Cache-busting                 | Simple version query string in fetch (`?v=2025-07-03`)                | Release notes                         |
| Cypress smoke test (optional) | Click through, assert score                                           | `tests/e2e_quiz.cy.js`                |

*Outcome:* HTML is now a static shell; content lives in JSON so slides → JSON → both PDF & HTML.

---

## Milestone 3 · PDF Generator CLI (2–3 days)

| Task               | Detail                                                                            | Deliverable                   |
| ------------------ | --------------------------------------------------------------------------------- | ----------------------------- |
| Directory scaffold | `generator/` with `__init__.py`, `templates/`                                     | Git structure                 |
| LaTeX templates    | `problem_set.tex.j2`, `solutions.tex.j2` (one per question, include explanations) | Template files                |
| Build script       | `build_ps.py --bank ../question_bank.json --out ./`                               | Executable                    |
| Pandoc fallback    | If LaTeX isn’t available, emit Markdown; document requirement                     | README note                   |
| Makefile helper    | `make pdf` calls CLI and `latexmk` twice                                          | Updated Makefile              |
| CI job             | GitHub Action: build, run `latexmk -pdf`, upload artifact                         | `.github/workflows/build.yml` |
| Lint & type-check  | `ruff`, `mypy` in pre-commit                                                      | Config files                  |

### `build_ps.py` outline

```python
#!/usr/bin/env python
import json, pathlib
from jinja2 import Environment, FileSystemLoader
from datetime import date

def load_bank(path):
    with open(path) as f:
        return json.load(f)["questions"]

def render(tex_tmpl, context, out_path):
    out_path.write_text(tex_tmpl.render(context))

def main():
    bank_path = pathlib.Path("question_bank.json")
    questions = load_bank(bank_path)
    env = Environment(loader=FileSystemLoader("templates"))
    ctx = {"questions": questions, "today": date.today()}
    for name in ("problem_set", "solutions"):
        render(env.get_template(f"{name}.tex.j2"), ctx, pathlib.Path(f"{name}.tex"))

if __name__ == "__main__":
    main()
```

---

## Milestone 4 · Deployment & DX Polish (ongoing)

* **Release workflow** – Push to `main`:

  1. Build PDFs
  2. Commit back to repo (or publish on GitHub Pages)
  3. Tag release `vN.M`
* **Auto-bump version** inside `script.js` and PDFs.
* **Contribution guide** (`CONTRIBUTING.md`): how to add slides → regenerate.
* **Future**: replace manual extraction with LLM-powered slide parser; migrate styling to Tailwind; add internationalisation.

---

### Estimated Timeline

| Phase               | Time     | Owner(s)         |
| ------------------- | -------- | ---------------- |
| M0 Audit & Schema   | 0.5 day  | Tech-lead + TA   |
| M1 Extract & JSON   | 1 day    | Python dev       |
| M2 Web-app refactor | 1.5 days | Front-end dev    |
| M3 Generator CLI    | 3 days   | Python/LaTeX dev |
| M4 Deploy polish    | rolling  | DevOps           |

**Total ≈ 6 developer-days** for a solid v1 transition.

