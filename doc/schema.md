# Question Bank Schema

All question banks use a structured JSON format so both the PDF generator and the web app can read the same data. Each question is a JSON object with the following fields:

- `id` *(int)* — Unique identifier within the problem set.
- `stem` *(string)* — The text of the question. Math should be written in LaTeX.
- `choices` *(array of objects)* — Available answer options. Each option has:
  - `key` *(string)* — Short label like `"a"`, `"b"`, etc.
  - `text` *(string)* — Option text (may include LaTeX).
  - `correct` *(bool)* — `true` only for the correct option.
- `explanation` *(string)* — Brief reasoning shown after the quiz is submitted.
- `tags` *(array of strings)* — Concept tags for search or curriculum mapping.
- `difficulty` *(string)* — Rough difficulty rating such as `"easy"`, `"medium"`, or `"hard"`.

This schema keeps the data independent from any rendering logic and is used by both the LaTeX templates and the client-side JavaScript grader.
