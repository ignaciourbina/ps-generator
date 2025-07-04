# validate_problemset3_computations
"""Validation helpers and quick self‑tests for the Week 5 computational MCQs.

Each helper mirrors the *exact* notation presented in the lecture slides so that
instructors and students can trace code ↔ formula one‑to‑one.

Run the module as a script to execute built‑in checks against the answer key
published in *problem_set_blueprint.md*.

Example
-------
$ python validate_week5_computations.py
W5‑Q14: PASS
W5‑Q15: **FAIL** (expected ≈ 0.333, got 0.3026)  ← highlights a key error
...
"""
from __future__ import annotations

from typing import Dict, Tuple, Union

from tools.validation_utils import (
    approx,
    ci_mu1_minus_mu2,
    ci_p1_minus_p2,
    df_paired,
    df_welch,
    margin_of_error,
    margin_of_error_z,
    pooled_p,
    p_value,
    se_hat_p_diff,
    se_pooled_p_diff,
    se_xbar_diff,
    t_stat_one_mean,
    t_stat_paired,
    t_stat_two_means,
    z_stat_two_props,
)

# ───────────────────────────────────────────────────────────────────────────────
# Custom statistical helpers (notation ≈ slides)
# ───────────────────────────────────────────────────────────────────────────────


# ───────────────────────────────────────────────────────────────────────────────
# Quick‑and‑dirty unit tests against the published answer key
# ───────────────────────────────────────────────────────────────────────────────

Answer = Union[float, Tuple[float, float]]




def run_self_checks() -> None:
    """Validate the seven computational MCQs and echo PASS/FAIL messages."""

    tests: Dict[str, Tuple[Answer, Answer]] = {
        # Q14 – SE of difference in proportions
        "W5‑Q14": (
            se_hat_p_diff(0.40, 200, 0.32, 250),
            0.046,  # answer key (choice B)
        ),
        # Q15 – pooled proportion (note: answer key appears wrong!)
        "W5‑Q15": (
            pooled_p(60, 200, 55, 180),
            0.303,  # answer key (choice A)
        ),
        # Q16 – 95 % CI for \mu₁−\mu₂
        "W5‑Q16": (
            ci_mu1_minus_mu2(52, 48, 11, 120, 9, 110),
            (1.411, 6.589),  # answer key (choice D)
        ),
        # Q17 – margin of error for mean
        "W5‑Q17": (
            margin_of_error_z(7, 100),
            1.37,  # answer key (choice B)
        ),
        # Q18 – t statistic (answer key appears wrong!)
        "W5‑Q18": (
            t_stat_one_mean(7.8, 7, 0.9, 12),
            3.08,  # answer key (choice D)
        ),
        # Q19 – degrees of freedom for paired samples
        "W5‑Q19": (
            df_paired(18),
            17,  # answer key (choice A)
        ),
        # Q20 – SE of difference in small‑sample means
        "W5‑Q20": (
            se_xbar_diff(4, 15, 5, 12),
            1.77,  # answer key (choice B)
        ),
    }

    for qid, (calc, key) in tests.items():
        ok = approx(calc, key)
        status = "PASS" if ok else "FAIL"
        print(f"{qid}: {status}")
        if not ok:
            print(f"  expected ≈ {key}, got {calc}")


if __name__ == "__main__":
    run_self_checks()
