# Problem Set 3 Answer Audit

This document records a question-by-question validation of the answers in
`problem-set-3/problem_set_blueprint.md`. Conceptual and interpretation
items are confirmed using direct quotations from the slide index. Numerical
items are verified by running `validate_problemset3_computations.py` and by
separate manual calculations.

## Procedure

1. Extract key lines from `lecture-slides/Slides_Index_Content.md` for each
   conceptual or interpretation question.
2. Execute the computation validation script with the repository root on the
   `PYTHONPATH`:
   ```bash
   PYTHONPATH=. python problem-set-3/validate_problemset3_computations.py
   ```
3. Independently re-compute the numeric answers using Python/`math`.

All validation checks passed. Details per question follow.

## Validation Details

### Conceptual & Interpretation Questions

- **W5-Q01** – Correct because the slide index lists the notation:
  ````text
  7. **Notation & Definitions** – $p_1,\,p_2,\;\hat p_1,\,\hat p_2,\;n_1,n_2$
  ````
- **W5-Q02** – Uses the CLT as noted:
  ````text
  13. **Sampling Distribution** – Approx. normal for large samples
  14. **Derivation Recap** – Uses CLT and independence.
  ````
- **W5-Q03** – Slide shows small-sample Student–t:
  ````text
  6. **Case 3: Small Sample (Unknown $\sigma^2$)** – Student‑t with $t_{n-1}$.
  ````
- **W5-Q04** – Adjusted-$Z$ formulas mention $\Delta_0$:
  ````text
  22. **Adjusted Z Formulas** – One & two means with $\mu_0,\,\Delta_0$.
  26. **Adjusted Z (Two Means)** – Statistic with $\Delta_0$.
  ````
- **W5-Q05** – Motivation for pairing:
  ````text
  15. **Why Pair?** – Removes between‑subject noise.
  ````
- **W5-Q06** – Decision tree for pooling variances:
  ````text
  26. **Pooling Variances** – Pooled $s_p^2$ & conditions.
  28. **Pooled vs Welch Decision Tree** – Flowchart.
  ````
- **W5-Q07** – Interpreting confidence intervals:
  ````text
  12. **Large‑Sample CI for $\mu_1-\mu_2$** – $(\bar X_1-\bar X_2)\pm z_{1-\alpha/2}SE$
  13. **Interpreting the CI** – Sign of interval.
  ````
- **W5-Q08** – Vaccination-rate example shows the interval crossing zero:
  ````text
  18. **Applied Example (Computation)** – $SE\approx0.032$; 95 % CI $[-0.013,0.113]$
  19. **Interpreting the CI** – Zero inside ⇒ no significant difference.
  ````
- **W5-Q09** – Sleep example with $Z=-2.67$:
  ````text
  18. **Hours of Sleep (Calc)** – $Z=-2.67$; reject at 5 %.
  ````
- **W5-Q10** – Turnout CI quote:
  ````text
  19. **Example – Turnout Pre/Post ID Law** – 95 % CI (−3.7, 0.1 pp).
  20. **Interpreting the CI** – Plausible range discussion.
  ````
- **W5-Q11** – Large-sample distribution of mean differences:
  ````text
  8. **Setup for Two Means** – Independent samples; statistic $\bar X_1-\bar X_2$.
  12. **Sampling Distribution (Large n)** – Approx. normal for $\bar X_1-\bar X_2$.
  ````
- **W5-Q12** – Definition of margin of error:
  ````text
  6. **Margin of Error** – $ME=z_{1-\alpha/2}\,SE$.
  ````
- **W5-Q13** – Slide notes multiple testing as a common trap:
  ````text
  31. **Common Traps** – Heteroskedasticity, imbalance, multiple testing.
  ````

### Computation Questions

Running the validation script produced:
```text
W5‑Q14: PASS
W5‑Q15: PASS
W5‑Q16: PASS
W5‑Q17: PASS
W5‑Q18: PASS
W5‑Q19: PASS
W5‑Q20: PASS
```

Manual calculations matched these values:
```text
SE: 0.046
p_hat: 0.303
CI: 1.411 6.589
ME: 1.37
T: 3.08
df: 17
SE_welch: 1.77
```

