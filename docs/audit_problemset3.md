# Audit of Problem Set 3 Blueprint

This report verifies all answers in `problem_set_3/problem_set_blueprint.md`.
We cross‑checked conceptual and interpretation items against the lecture
slides and validated every numerical item using the helper script
`validate_problemset3_computations.py` plus manual calculations.

## Procedure
1. **Slide verification** – For each conceptual or interpretation question the
   relevant lecture PDF was searched using `pdftotext`. A short quote or bullet
   confirming the correct answer is recorded below with the slide reference.
2. **Computation checks** – `python problem-set-3/validate_problemset3_computations.py`
   was executed with `PYTHONPATH=.`, producing PASS/FAIL status for each
   quantitative question. Manual calculations with Python confirmed the results.

## Results by Question

### Conceptual and Interpretation Items
| QID | Slide Evidence |
| --- | --- |
| **W5-Q01** | "Let p1 and p2 represent the population proportions for two independent groups" (Lecture 9, slide 7). |
| **W5-Q02** | "The distribution of p̂₁−p̂₂ is approximately normal for large sample sizes. Under the Central Limit Theorem…" (Lecture 9, slide 13). |
| **W5-Q03** | "If n is small (n < 30) and σ² is unknown… we use the t-distribution" (Lecture 10, slide 6). |
| **W5-Q04** | "Adjusted Z Formulas – One & two means with μ₀, Δ₀" (Lecture 11, slide 22). |
| **W5-Q05** | "Why Pair? – Removes between-subject noise" (Lecture 12, slide 15). |
| **W5-Q06** | "Use pooled t only when: … Sample sizes are not wildly unequal" (Lecture 12, slide 26). |
| **W5-Q07** | "Interpreting the CI – Zero inside ⇒ no significant difference" (Lecture 11, slide 19). |
| **W5-Q08** | Same CI example as slide evidence above; interval crosses zero so no significant difference. |
| **W5-Q09** | "Hours of Sleep (Calc) – Z = -2.67; reject at 5%" (Lecture 11, slide 18). |
| **W5-Q10** | "Example–Turnout Pre/Post ID Law – 95% CI (-3.7, 0.1 pp)" (Lecture 12, slide 19). |
| **W5-Q11** | "Case  2: Large Sample (CLT) – Approx. normal regardless of population shape" (Lecture 10, slide 4). |
| **W5-Q12** | "Margin of Error – ME = z₁−α⁄₂ SE" (Lecture 11, slide 6). |
| **W5-Q13** | "Common Traps – Heteroskedasticity, imbalance, multiple testing" (Lecture 12, slide 31). |

### Computation Items
The validation script produced:
```
W5-Q14: PASS
W5-Q15: PASS
W5-Q16: PASS
W5-Q17: PASS
W5-Q18: PASS
W5-Q19: PASS
W5-Q20: PASS
```
Manual Python calculations matched these results:
```
Q14 SE  ≈ 0.0455
Q15 p̂ ≈ 0.3026
Q16 CI ≈ (1.41, 6.59)
Q17 ME ≈ 1.372
Q18 t  ≈ 3.08
Q19 df = 17
Q20 SE ≈ 1.77
```

All answers in the blueprint are therefore consistent with the lecture material
and numerical checks.
