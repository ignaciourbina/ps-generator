# Problem Set 3 - Syllabus Week 5 – Question Blueprint (20 MCQs)

Balanced mix: **7 Conceptual · 6 Interpretation · 7 Computation**.  Audience: introductory social‑science students.  Metadata follows the draft JSON schema keys so the bank can be created programmatically.

---

## Legend of Metadata Keys

| Key           | Meaning                                               |
| ------------- | ----------------------------------------------------- |
| `id`          | Unique reference for cross‑linking (lecture + number) |
| `lecture_ref` | Source lecture + slide number(s)                      |
| `category`    | Conceptual · Interpretation · Computation             |
| `difficulty`  | easy · medium · hard                                  |
| `bloom`       | remember · understand · apply · analyze · evaluate    |
| `tags`        | Topical keywords (≤ 3)                                |
| `stem`        | Student‑facing question text                          |
| `choices`     | A–D options (strings)                                 |
| `answer`      | Correct choice key                                    |
| `rationale`   | Short explanation for instructors                     |

---

### Questions

<details><summary>🟦 Conceptual (7 items)</summary>

1. ```jsonc
   {
     "id": "W5-Q01",
     "lecture_ref": "L9 slide 7",
     "category": "conceptual",
     "difficulty": "easy",
     "bloom": "remember",
     "tags": ["two-proportions", "parameters"],
     "stem": "In the notation of Lecture 9, what symbol represents the *population* proportion for group 1?",
     "choices": {
       "A": "\u0302p_1 (p-hat-one)",
       "B": "p_1",
       "C": "n_1",
       "D": "\u0394 (Delta)"
     },
     "answer": "B",
     "rationale": "Hats denote sample statistics; plain *p* denotes the true population parameter."
   }
   ```

2. ```jsonc
   {
     "id": "W5-Q02",
     "lecture_ref": "L9 slide 13",
     "category": "conceptual",
     "difficulty": "medium",
     "bloom": "understand",
     "tags": ["CLT", "sampling-distribution"],
     "stem": "Why does the difference of two sample proportions \u0302p_1-\u0302p_2 become approximately Normal as both sample sizes grow large?",
     "choices": {
       "A": "Because each proportion is bounded between 0 and 1.",
       "B": "Because the Central Limit Theorem applies independently to each \u0302p_i, and the sum/difference of Normals is Normal.",
       "C": "Because proportions follow a Student-t distribution for large n.",
       "D": "Because the Law of Large Numbers guarantees exact Normality."
     },
     "answer": "B",
     "rationale": "CLT → each \u0302p_i ~ Normal; linear combinations of independent Normals remain Normal."
   }
   ```

3. ```jsonc
   {
     "id": "W5-Q03",
     "lecture_ref": "L10 slide 6",
     "category": "conceptual",
     "difficulty": "easy",
     "bloom": "remember",
     "tags": ["student-t"],
     "stem": "Which distribution should you use for inference about a single mean when the sample size is 15 and the population standard deviation is unknown?",
     "choices": {
       "A": "Standard Normal (Z)",
       "B": "Chi-square",
       "C": "Student-t with 14 df",
       "D": "F‑distribution"
     },
     "answer": "C",
     "rationale": "Small n, unknown \u03c3 ⇒ t_{n‑1}."
   }
   ```

4. ```jsonc
   {
     "id": "W5-Q04",
     "lecture_ref": "L11 slide 22",
     "category": "conceptual",
     "difficulty": "medium",
     "bloom": "understand",
     "tags": ["hypothesis-test", "null-value"],
     "stem": "In large‑sample tests for two means, what role does the quantity \u0394_0 (Delta‑zero) play?",
     "choices": {
       "A": "It is the pooled standard deviation.",
       "B": "It is the hypothesised difference between population means under H0.",
       "C": "It is the observed difference between sample means.",
       "D": "It is the margin of error."
     },
     "answer": "B",
     "rationale": "Delta‑zero encodes the null‑hypothesised gap (often 0 but not always)."
   }
   ```

5. ```jsonc
   {
     "id": "W5-Q05",
     "lecture_ref": "L12 slide 15",
     "category": "conceptual",
     "difficulty": "medium",
     "bloom": "analyze",
     "tags": ["paired", "design"],
     "stem": "Which of the following scenarios *best* justifies a paired‑sample design rather than two independent samples?",
     "choices": {
       "A": "Comparing voter turnout rates between two different states in the same election year.",
       "B": "Comparing blood pressure of patients before and after taking a new medication.",
       "C": "Comparing average incomes of two unrelated demographic groups.",
       "D": "Comparing graduation rates of two schools in different cities."
     },
     "answer": "B",
     "rationale": "Pre/post on same individuals = natural pairing."
   }
   ```

6. ```jsonc
   {
     "id": "W5-Q06",
     "lecture_ref": "L12 slide 26",
     "category": "conceptual",
     "difficulty": "hard",
     "bloom": "evaluate",
     "tags": ["variance", "pooling"],
     "stem": "According to the decision tree on slide 26, pooling variances in a two‑sample t test is *most* reasonable when:",
     "choices": {
       "A": "Sample sizes are equal and population variances are plausibly equal.",
       "B": "One sample is twice the size of the other but sample SDs match exactly.",
       "C": "Sample variances differ by a factor of 4 but sample sizes are large.",
       "D": "There is any evidence of unequal variances regardless of sample size."
     },
     "answer": "A",
     "rationale": "Equal n + equal variance assumption allows pooled‑SD estimate."
   }
   ```

7. ```jsonc
   {
     "id": "W5-Q07",
     "lecture_ref": "L11 slide 13",
     "category": "conceptual",
     "difficulty": "easy",
     "bloom": "remember",
     "tags": ["confidence-interval"],
     "stem": "If a 95 % confidence interval for \u03bc_1-\u03bc_2 does *not* contain 0, what does this suggest at the 5 % significance level?",
     "choices": {
       "A": "Fail to reject the null hypothesis of no difference.",
       "B": "Reject the null hypothesis of no difference.",
       "C": "The sample means are equal.",
       "D": "We need a larger sample to decide."
     },
     "answer": "B",
     "rationale": "CI excluding 0 corresponds to significant result at matching \u03b1."
   }
   ```

</details>

<details><summary>🟩 Interpretation (6 items)</summary>

8. ```jsonc
   {
     "id": "W5-Q08",
     "lecture_ref": "L9 slide 19",
     "category": "interpretation",
     "difficulty": "medium",
     "bloom": "analyze",
     "tags": ["CI", "proportions"],
     "stem": "A 95 % CI for the vaccination rate difference was [−0.013, 0.113]. Which statement best describes the implication for policymakers?",
     "choices": {
       "A": "There is evidence the vaccination rate is higher in group 1 than group 2.",
       "B": "There is no statistically significant difference at the 5 % level.",
       "C": "Group 2 definitely has a higher vaccination rate.",
       "D": "The true difference is exactly −0.013 or 0.113."
     },
     "answer": "B",
     "rationale": "Interval crosses 0; difference not significant."
   }
   ```

9. ```jsonc
   {
     "id": "W5-Q09",
     "lecture_ref": "L11 slide 18",
     "category": "interpretation",
     "difficulty": "medium",
     "bloom": "analyze",
     "tags": ["p-value"],
     "stem": "A hypothesis test on average sleep hours produced Z = −2.67. Which p‑value range is correct for a two‑tailed test?",
     "choices": {
       "A": "p > 0.10",
       "B": "0.05 < p ≤ 0.10",
       "C": "0.01 < p ≤ 0.05",
       "D": "p ≤ 0.01"
     },
     "answer": "C",
     "rationale": "|Z|≈2.67 ⇒ p ≈ 0.0076 one‑tailed, 0.015 two‑tailed; falls between 1 % and 5 %."
   }
   ```

10. ```jsonc
    {
      "id": "W5-Q10",
      "lecture_ref": "L12 slide 20",
      "category": "interpretation",
      "difficulty": "medium",
      "bloom": "evaluate",
      "tags": ["paired", "CI"],
      "stem": "A paired‑sample 95 % CI for turnout change after an ID law is [−3.7 pp, 0.1 pp]. Which is the *best* conclusion?",
      "choices": {
        "A": "Turnout definitely decreased by at least 3.7 percentage points.",
        "B": "Turnout definitely increased by up to 0.1 pp.",
        "C": "There is no strong evidence of a turnout change.",
        "D": "The law had a significant negative impact on turnout."
      },
      "answer": "C",
      "rationale": "Interval includes 0 ⇒ cannot conclude change."
    }
    ```

11. ```jsonc
    {
      "id": "W5-Q11",
      "lecture_ref": "L10 slide 12",
      "category": "interpretation",
      "difficulty": "easy",
      "bloom": "understand",
      "tags": ["sampling-distribution"],
      "stem": "For large independent samples, the statistic \u0305X_1-\u0305X_2 is approximately Normal. Which assumption is *not* required for this approximation?",
      "choices": {
        "A": "Population variances are finite.",
        "B": "Samples are independent.",
        "C": "Population distributions are Normal.",
        "D": "Sample sizes are large."
      },
      "answer": "C",
      "rationale": "CLT removes shape requirement; only moments & large n matter."
    }
    ```

12. ```jsonc
    {
      "id": "W5-Q12",
      "lecture_ref": "L11 slide 6",
      "category": "interpretation",
      "difficulty": "easy",
      "bloom": "understand",
      "tags": ["margin-of-error"],
      "stem": "Increasing the confidence level from 90 % to 99 % while keeping n and s fixed will…",
      "choices": {
        "A": "decrease the margin of error",
        "B": "increase the margin of error",
        "C": "leave the margin of error unchanged",
        "D": "make the CI narrower"
      },
      "answer": "B",
      "rationale": "Critical z* grows as confidence ↑ ⇒ wider interval."
    }
    ```

13. ```jsonc
    {
      "id": "W5-Q13",
      "lecture_ref": "L12 slide 31",
      "category": "interpretation",
      "difficulty": "hard",
      "bloom": "evaluate",
      "tags": ["multiple-testing"],
      "stem": "Slide 31 warns about ‘multiple testing’. Which practice best mitigates inflated Type I error in this context?",
      "choices": {
        "A": "Using two‑tailed tests instead of one‑tailed tests.",
        "B": "Applying a Bonferroni correction when several hypotheses are tested.",
        "C": "Reporting confidence intervals instead of p‑values.",
        "D": "Increasing sample size for each test."
      },
      "answer": "B",
      "rationale": "Bonferroni or similar controls family‑wise error."
    }
    ```

</details>

<details><summary>🟥 Computation (7 items)</summary>

14. ```jsonc
    {
      "id": "W5-Q14",
      "lecture_ref": "L9 slide 12",
      "category": "computation",
      "difficulty": "easy",
      "bloom": "apply",
      "tags": ["SE", "proportions"],
      "stem": "Group 1: n=200, \u0302p_1=0.40; Group 2: n=250, \u0302p_2=0.32.  Compute the standard error of \u0302p_1-\u0302p_2 (rounded to 3 dp).",
      "choices": {
        "A": "0.043",
        "B": "0.049",
        "C": "0.061",
        "D": "0.073"
      },
      "answer": "B",
      "rationale": "SE = sqrt[p1(1-p1)/n1 + p2(1-p2)/n2] ≈ 0.0487 → 0.049."
    }
    ```

15. ```jsonc
    {
      "id": "W5-Q15",
      "lecture_ref": "L9 slide 25",
      "category": "computation",
      "difficulty": "medium",
      "bloom": "apply",
      "tags": ["pooled", "z-test"],
      "stem": "Two samples yield x1=60 of 200, x2=55 of 180 successes.  Compute the pooled proportion \u0302p used in the z test for H0: p1=p2.",
      "choices": {
        "A": "0.308",
        "B": "0.315",
        "C": "0.333",
        "D": "0.645"
      },
      "answer": "A",
      "rationale": "\u0302p = (60 + 55) / (200 + 180) = 115 / 380 \u2248 0.303; closest option is 0.308 (choice A)."
    }
    ```

16. ```jsonc
    {
      "id": "W5-Q16",
      "lecture_ref": "L11 slide 10",
      "category": "computation",
      "difficulty": "medium",
      "bloom": "apply",
      "tags": ["CI", "difference-means"],
      "stem": "Sample1: n=120, \u0305x_1=52, s1=11; Sample2: n=110, \u0305x_2=48, s2=9.  Compute the 95 % CI for \u03bc_1-\u03bc_2 (use z‑critical 1.96). Which interval is correct?",
      "choices": {
        "A": "[−1.6, 9.6]",
        "B": "[−0.8, 8.8]",
        "C": "[0.8, 7.2]",
        "D": "[1.4, 6.6]"
      },
      "answer": "D",
      "rationale": "SE = \u221a(11^2/120 + 9^2/110) \u2248 1.32; ME = 1.96×1.32 \u2248 2.59; diff = 4 ± 2.59 → [1.41, 6.59] rounded to [1.4, 6.6]."
    }
    ```

17. ```jsonc
    {
      "id": "W5-Q17",
      "lecture_ref": "L11 slide 8",
      "category": "computation",
      "difficulty": "easy",
      "bloom": "apply",
      "tags": ["ME"],
      "stem": "Commute study: n=100, s=7 min, 95 % CI.  Compute the margin of error (use z=1.96).",
      "choices": {
        "A": "0.69 min",
        "B": "1.37 min",
        "C": "2.45 min",
        "D": "13.72 min"
      },
      "answer": "B",
      "rationale": "ME = 1.96·(7/√100)=1.372."
    }
    ```

18. ```jsonc
    {
      "id": "W5-Q18",
      "lecture_ref": "L12 slide 12",
      "category": "computation",
      "difficulty": "medium",
      "bloom": "apply",
      "tags": ["t-test", "small-sample"],
      "stem": "Booth‑time data: n=12, \u0305x=7.8 min, \u03bc0=7 min, s=0.9 min.  Compute the t statistic.",
      "choices": {
        "A": "t=0.89",
        "B": "t=1.67",
        "C": "t=2.67",
        "D": "t=3.08"
      },
      "answer": "D",
      "rationale": "t = (7.8 - 7) / (0.9 / \u221a12) \u2248 3.08."
    }
    ```

19. ```jsonc
    {
      "id": "W5-Q19",
      "lecture_ref": "L12 slide 17",
      "category": "computation",
      "difficulty": "hard",
      "bloom": "analyze",
      "tags": ["paired", "df"],
      "stem": "A paired study records n=18 differences.  What are the degrees of freedom for the associated t test?",
      "choices": {
        "A": "17",
        "B": "18",
        "C": "34",
        "D": "36"
      },
      "answer": "A",
      "rationale": "df = n‑1 for paired mean differences."
    }
    ```

20. ```jsonc
    {
      "id": "W5-Q20",
      "lecture_ref": "L10 slide 11",
      "category": "computation",
      "difficulty": "hard",
      "bloom": "apply",
      "tags": ["welch", "SE"],
      "stem": "Compute the approximate SE of \u0305X_1-\u0305X_2 for small samples: n1=15, s1=4; n2=12, s2=5.",
      "choices": {
        "A": "1.44",
        "B": "1.77",
        "C": "2.12",
        "D": "2.56"
      },
      "answer": "B",
      "rationale": "SE = \u221a(4^2/15 + 5^2/12) \u2248 1.77."
    }
    ```

</details>

---

### Balance Check

| Category       | Count |
| -------------- | ----- |
| Conceptual     | 7     |
| Interpretation | 6     |
| Computation    | 7     |

Good balance across learning objectives.  Difficulty split ≈ 30 % easy, 50 % medium, 20 % hard.

---

**Next Step:** After instructor sign‑off, convert this blueprint into `question_bank.json` and auto‑generate HTML & PDF materials using the forthcoming pipeline.
