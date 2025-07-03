# Problem Set Generator

### 1. What the project is for

- **Purpose** – A light-weight pipeline that lets an instructor collect lecture slides, auto-generate weekly problem-sets, and give students a quick self-check web page.
- **Audience** – Students in an introductory probability / data-science course.
- **Output formats** – PDF (formal problem set and solutions sheet) plus a small, static HTML “quiz” that grades itself client-side.

---

### 2. Top-level organisation

| Folder            | Role                                      | Typical contents (seen or strongly implied)                                                                                                                                               |
| ----------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **problem-set-1** | One fully-packaged weekly unit            | • `lecture-slides/` – PDFs of that week’s lecture<br>• `web_app/` – a tiny self-assessment site<br>• (usually) `bank/` or `generator/` scripts that build the PDF problem set & solutions |
| **problem-set-2** | ...                                       | ...                                                                                                                                                                                       |
| **problem-set-3** | Future units that follow the same pattern | Skeleton scaffolds plus a question blueprint (`problem_set_blueprint.md`) and a validation script                                                                                         |
| **LICENSE**       | Standard MIT license                      | No code impact                                                                                                                                                                            |

> **Design pattern** – Each _problem-set-N_ directory is deliberately **self-contained**: you can zip it, hand it to a TA, or deploy just that week’s mini-site without touching the rest of the repo. That keeps semester-to-semester edits local.

---

### 3. Repo File Structure

| Path                                                                            | What it is                                                             | Key take-aways                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `problem-set-1/lecture-slides/W2 - Lecture 4 - Introduction to Probability.pdf` | 35-ish slide deck that the generator bundles alongside the problem set | Covers sample spaces, events, conditional probability, the Law of Total Probability, Bayes, PMF/PDF, expectation & variance (judging by the file name and the week-2 slot). Students have the “theory” right next to the practice problems. |
| `problem-set-1/web_app/index.html`                                              | The self-assessment page                                               | Extremely small and Markdown-like – literally starts with “# Probability Self-Assessment” followed by the quiz text. The questions themselves are embedded right in the HTML (no build step) so GitHub Pages can host it instantly.         |
| `problem-set-1/web_app/style.css`                                               | Minimal CSS to make it presentable                                     | In 300 bytes it sets a modern system font, uses a single **.card** container, and tightens typography. The goal is “looks OK on mobile without frameworks”.                                                                                 |
| `doc/`                                                                          | Internal documentation                                                 | `audit_ps1_ps2.md` captures an audit of sets 1–2, while `schema.md` defines the JSON question format                                                                                                                                        |

**How the mini-site works**

1. The HTML declares each question as a `<fieldset>` of radio buttons.
2. A few lines of inline JavaScript (very likely sitting at the bottom of the same file) iterate over chosen answers, compare them to a hard-coded answer key, then inject feedback into the DOM.
3. The CSS makes the whole thing sit in a centered card so it feels like an “app”, not a raw HTML page.

No build tools, no dependencies – students just open the file.

---

### 4. How to extend or maintain

- **Centralise the answer key for each problem set** – Expose it as `answers.json`
- **Accessibility pass** – Wrap radio groups with `<legend>`s, add ARIA `aria-live="polite"` to the results area for screen-reader friendliness.
- **Lint CSS** – As the course grows, migrate the ad-hoc CSS to a mini utility class file or Tailwind to avoid style drift.
- - **Question bank** – YAML/JSON/CSV files with question text, variables, and correct answers.
- **Jinja/LaTeX templates** – A Python script walks the bank, renders LaTeX, and spits out “Problem Set 1.pdf” and “Solutions 1.pdf”.
- **Makefile or runner script** – One-liner to rebuild everything when questions change.
- **Question extraction utility** – Run `tools/extract_questions.py` to export a `question_bank.json` from any `web_app/index.html`.

---

### 5. TL;DR cheat sheet

- **Each problem-set directory = one week’s slides + web quiz.**
- **PDFs give the theory; the web quiz gives immediate feedback.**
- **No heavyweight stacks – everything is static so it works on GitHub Pages or Canvas.**

### 6. Extracting question banks

Run the helper script to convert an existing web quiz into a JSON question bank:

```bash
python tools/extract_questions.py problem-set-N/web_app/index.html \
    problem-set-N/question_bank.json
```

Replace `N` with the desired week number.

---

### 7. Project status & testing

Two full problem sets are currently published:

- **Problem Set 1** – 14 questions on introductory probability.
- **Problem Set 2** – 21 questions covering the basics of inference.

Problem Set 3 contains a draft blueprint and validation helpers. Once its web
quiz is ready you can run the same extraction step to produce
`question_bank.json`.

Run the test suite to confirm the question banks load correctly:

```bash
pytest -q
```

HTML files can be checked with `tidy` and formatted with `prettier`.
