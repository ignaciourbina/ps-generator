# Ticket: Align Problem Set 3 Blueprint with Validation Output

**File:** `problem_set_blueprint.md`

The validation script `validate_problemset3_computations.py` was executed and is treated as the canonical source for numerical answers. The following discrepancies were observed between the script output and the blueprint. Only questions with mismatched values require edits.

| QID | Issue | Required Fix |
| --- | ----- | ------------ |
| **W5-Q14** | Blueprint lists choice **B** = `0.049` and rationale uses `0.0487`, but validation computes `0.0455` (≈ `0.046`). | Update choice B to `0.046` and adjust rationale accordingly. |
| **W5-Q15** | Blueprint choice **A** = `0.308`; validation computes `0.3026` (≈ `0.303`). | Change choice A to `0.303` and mention the exact calculation `115/380 ≈ 0.303` in the rationale. |
| **W5-Q16** | Validation gives `(1.411, 6.589)` ⇒ `[1.4, 6.6]` which already matches choice **D**. | No change required. |
| **W5-Q18** | Validation gives `t=3.079` ⇒ `3.08`; blueprint choice **D** already matches. | No change required. |
| **W5-Q20** | Validation gives `SE=1.775` ⇒ `1.77`; blueprint choice **B** already matches. | No change required. |

These edits will synchronize the blueprint with the validated computations and prevent future discrepancies.
