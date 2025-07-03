# Problem Set Generator 

### 1. What the project is for

* **Purpose** – A light-weight pipeline that lets an instructor collect lecture slides, auto-generate weekly problem-sets, and give students a quick self-check web page.
* **Audience** – Students in an introductory probability / data-science course.
* **Output formats** – PDF (formal problem set and lecture slides) plus a small, static HTML “quiz” that grades itself client-side.

---

### 2. Top-level organisation

| Folder                               | Role                                      | Typical contents (seen or strongly implied)                                                                                                                                               |
| ------------------------------------ | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **problem-set-1**                    | One fully-packaged weekly unit            | • `lecture-slides/` – PDFs of that week’s lecture<br>• `web_app/` – a tiny self-assessment site<br>• (usually) `bank/` or `generator/` scripts that build the PDF problem set & solutions |
| **problem-set-2** | ... | ...                                                                                                                          |
| **problem-set-3** | Future units that follow the same pattern | Skeletons waiting for their own slides / web\_app / generator                                                                                                                             |
| **LICENSE**                          | Standard MIT license                      | No code impact                                                                                                                                                                            |

> **Design pattern** – Each *problem-set-N* directory is deliberately **self-contained**: you can zip it, hand it to a TA, or deploy just that week’s mini-site without touching the rest of the repo. That keeps semester-to-semester edits local.

---

### 3. Deep-dive into the pieces you linked

| Path                                                                            | What it is                                                             | Key take-aways                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `problem-set-1/lecture-slides/W2 - Lecture 4 - Introduction to Probability.pdf` | 35-ish slide deck that the generator bundles alongside the problem set | Covers sample spaces, events, conditional probability, the Law of Total Probability, Bayes, PMF/PDF, expectation & variance (judging by the file name and the week-2 slot). Students have the “theory” right next to the practice problems.                          |
| `problem-set-1/web_app/index.html`                                              | The self-assessment page                                               | Extremely small and Markdown-like – literally starts with “# Probability Self-Assessment” followed by the quiz text. The questions themselves are embedded right in the HTML (no build step) so GitHub Pages can host it instantly. ([raw.githubusercontent.com][1]) |
| `problem-set-1/web_app/style.css`                                               | Minimal CSS to make it presentable                                     | In 300 bytes it sets a modern system font, uses a single **.card** container, and tightens typography. The goal is “looks OK on mobile without frameworks”. ([raw.githubusercontent.com][2])                                                                         |

**How the mini-site works**

1. The HTML declares each question as a `<fieldset>` of radio buttons.
2. A few lines of inline JavaScript (very likely sitting at the bottom of the same file) iterate over chosen answers, compare them to a hard-coded answer key, then inject feedback into the DOM.
3. The CSS makes the whole thing sit in a centered card so it feels like an “app”, not a raw HTML page.

No build tools, no dependencies – students just open the file.

---

### 4. The hidden but typical pieces

Even though you didn’t point to them directly, a problem-set-*generator* repo almost always contains:

* **Question bank** – YAML/JSON/CSV files with question text, variables, and correct answers.
* **Jinja/LaTeX templates** – A Python script walks the bank, renders LaTeX, and spits out “Problem Set 1.pdf” and “Solutions 1.pdf”.
* **Makefile or runner script** – One-liner to rebuild everything when questions change.

You can spot traces of this in the naming conventions (“generator” in the repo name and the fact that the HTML quiz hard-codes its answers – the same answer key probably seeds both the PDF and the web app).

---

### 5. How to extend or maintain

* **Centralise the answer key** – Expose it as `answers.json` so the PDF generator and the web quiz read the *same* file.
* **Add CI** – GitHub Actions step: run the generator, commit the freshly built PDFs to `gh-pages`, and push the HTML quiz to Pages automatically.
* **Componentise the web app** – Switch to a tiny framework (Preact / Alpine) only if you want dynamic question loading; otherwise your present simple HTML + vanilla JS is perfect.
* **Accessibility pass** – Wrap radio groups with `<legend>`s, add ARIA `aria-live="polite"` to the results area for screen-reader friendliness.
* **Lint CSS** – As the course grows, migrate the ad-hoc CSS to a mini utility class file or Tailwind to avoid style drift.

---

### 6. TL;DR cheat sheet

* **Each problem-set directory = one week’s slides + PDF generator + web quiz.**
* **PDFs give the theory; the web quiz gives immediate feedback.**
* **No heavyweight stacks – everything is static so it works on GitHub Pages or Canvas.**
