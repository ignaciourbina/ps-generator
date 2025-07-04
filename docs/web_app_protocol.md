# Web App Structure and Metadata Protocol

This document explains how the self‑assessment web apps are organized for Problem Sets 1 and 2 and describes a protocol for building new problem set apps from a question bank JSON.

## Folder Layout
Each `problem-set-N/` directory is self contained:

```
problem-set-N/
├── lecture-slides/            # Source PDFs
├── question_bank.json         # Array of question objects
└── web_app/
    ├── index.html             # Static page
    ├── style.css (or styles.css)
    └── script.js              # Client-side grader
```

The web app uses only these static files and can be hosted on GitHub Pages or any static server without a build step.

## Question Bank Format
Both Problem Set 1 and Problem Set 2 store questions in a single JSON array. The objects share the following fields:

- `id` – numeric identifier unique within the set.
- `text` – question wording (LaTeX allowed).
- `topic_short` – short label used in the results view.
- `options` – array of answer choices, each with:
  - `text` – option text (supports LaTeX).
  - `value` – short key such as `"a"`, `"b"`, etc.
- `correctAnswer` – the matching option `value`.
- `explanation` – short feedback shown after submitting.

Additional metadata (e.g. difficulty, tags) can be added as needed; `script.js` will ignore unknown fields, so the structure is forward‑compatible.

## How the Web App Works
`index.html` loads `script.js`, which fetches `question_bank.json` and dynamically renders each question. The script:
1. Shuffles answer options for randomness.
2. Tracks user selections.
3. After submission, shows a summary and per‑question explanations.
4. Uses MathJax for rendering LaTeX in both questions and answers.

Because all data comes from `question_bank.json`, the same `script.js` works across problem sets with no modification beyond an optional cache‑busting version constant.

## Protocol for Creating a New Problem Set Web App
1. **Create the directory** `problem-set-X/` and copy the `web_app/` folder from an existing set.
2. **Prepare `question_bank.json`** following the schema above. Ensure each question object includes the required fields.
3. **Edit `index.html`** to update the page title and introductory text for the new topic.
4. Optionally bump the `CACHE_VERSION` constant in `script.js` to force browsers to reload the question bank.
5. Place any lecture PDFs in `lecture-slides/` for reference.
6. Commit the new directory. The app will run entirely from these files—no external dependencies beyond MathJax and Tailwind CDN links in `index.html`.

## Converting Blueprint Markdown

When instructors provide a Markdown blueprint containing JSON question objects (as in `problem-set-3/problem_set_blueprint.md`), run a small parser to transform the blocks into `question_bank.json`.

1. Extract each fenced `jsonc` code block.
2. Convert the blueprint keys to the minimal bank schema:
   - `stem` → `text`
   - first tag from `tags` → `topic_short`
   - `choices` → array of `{text, value}` with values `a`–`d`
   - `answer` → `correctAnswer` (lower‑cased)
   - `rationale` → `explanation`
3. Number the items sequentially as the `id` field.

The helper script `problem-set-3/parse_blueprint.py` demonstrates this process for Week 5 and writes `question_bank.json` in the same folder.

Following this protocol ensures each problem set is independent and can be zipped or hosted individually. Future enhancements, such as additional metadata fields or styling changes, can be incorporated without breaking existing sets as long as the core JSON structure remains an array of question objects with the fields listed above.
