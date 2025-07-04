# Validation Audit for Problem Set 3

The script `validate_problemset3_computations.py` was reviewed and executed.
Several issues were found and corrected:

- The default tolerance value used an en dash (`5e–3`) causing a `SyntaxError`.
  Replaced with `5e-3`.
- Docstrings containing LaTeX expressions triggered `SyntaxWarning` due to
  unescaped backslashes. They were converted to raw strings and properly
  indented.
- Reference to *Week5-Question-Blueprint.md* was updated to the actual file
  name `problem_set_blueprint.md`.
- Output formatting for failing tests now handles tuples correctly.

After fixes, the validation script produced the following output:

```
W5‑Q14: PASS
W5‑Q15: FAIL
  expected ≈ 0.333, got 0.3026315789473684
W5‑Q16: FAIL
  expected ≈ (1.6, 6.4), got (1.4110952356666577, 6.588904764333343)
W5‑Q17: PASS
W5‑Q18: FAIL
  expected ≈ 2.67, got 3.079201435678003
W5‑Q19: PASS
W5‑Q20: FAIL
  expected ≈ 1.87, got 1.7748239349298849
```

Questions 15, 16, 18 and 20 deviate from the published answer key and should be
reviewed.
