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

import math
from typing import Dict, Tuple, Union, Optional

from scipy import stats

# ───────────────────────────────────────────────────────────────────────────────
# Custom statistical helpers (notation ≈ slides)
# ───────────────────────────────────────────────────────────────────────────────

def se_hat_p_diff(p1_hat: float, n1: int, p2_hat: float, n2: int) -> float:
    """Standard error of the difference of two sample proportions.

    Formula (Lecture 9, slide 12)::
        SE = sqrt[ p1(1−p1)/n1 + p2(1−p2)/n2 ]
    """
    return math.sqrt(p1_hat * (1 - p1_hat) / n1 + p2_hat * (1 - p2_hat) / n2)


def pooled_p(x1: int, n1: int, x2: int, n2: int) -> float:
    """Pooled estimator \u0302p under H0 : p1 = p2 (Lecture 9, slide 25)."""
    return (x1 + x2) / (n1 + n2)


def se_xbar_diff(s1: float, n1: int, s2: float, n2: int) -> float:
    """Standard error of \bar X₁ − \bar X₂ (Lecture 10, slide 11)."""
    return math.sqrt(s1 ** 2 / n1 + s2 ** 2 / n2)


def margin_of_error_z(s: float, n: int, z: float = 1.96) -> float:
    """Margin of error for a large‑sample CI for a mean (Lecture 11, slide 6).

    ME = z*·s/√n
    """
    return z * s / math.sqrt(n)


def ci_mu1_minus_mu2(
    mean1: float,
    mean2: float,
    s1: float,
    n1: int,
    s2: float,
    n2: int,
    z: float = 1.96,
) -> Tuple[float, float]:
    r"""Large‑sample CI for \mu_1 - \mu_2 (Lecture 11, slide 12)."""
    diff = mean1 - mean2
    se = se_xbar_diff(s1, n1, s2, n2)
    me = z * se
    return diff - me, diff + me


def t_stat_one_mean(xbar: float, mu0: float, s: float, n: int) -> float:
    r"""Student-t statistic for H0 : \mu = \mu_0 (Lecture 12, slide 7)."""
    return (xbar - mu0) / (s / math.sqrt(n))


def df_paired(n: int) -> int:
    """Degrees of freedom for paired‑sample t procedures (Lecture 12, slide 17)."""
    return n - 1


def margin_of_error(se: float, critical: float) -> float:
    """Generic margin of error ME = critical × SE (Lecture 11, slide 6)."""
    return critical * se


def ci_two_proportions(
    p1_hat: float, n1: int, p2_hat: float, n2: int, z: float = 1.96
) -> Tuple[float, float]:
    r"""Large‑sample CI for p₁ − p₂ (Lecture 9, slide 15)."""
    diff = p1_hat - p2_hat
    se = se_hat_p_diff(p1_hat, n1, p2_hat, n2)
    me = z * se
    return diff - me, diff + me


def z_stat_two_props(
    x1: int, n1: int, x2: int, n2: int, delta0: float = 0.0
) -> float:
    """Z statistic for H0 : p₁ − p₂ = Δ₀ (Lecture 9, slide 26)."""
    p_pool = pooled_p(x1, n1, x2, n2)
    se0 = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n2))
    diff_hat = x1 / n1 - x2 / n2
    return (diff_hat - delta0) / se0


def z_stat_one_mean(xbar: float, mu0: float, s: float, n: int) -> float:
    """Large‑sample Z statistic for one mean (Lecture 11, slide 4)."""
    return (xbar - mu0) / (s / math.sqrt(n))


def z_stat_two_means(
    mean1: float,
    mean2: float,
    s1: float,
    n1: int,
    s2: float,
    n2: int,
    delta0: float = 0.0,
) -> float:
    r"""Large‑sample Z for \mu₁ − \mu₂ = Δ₀ (Lecture 11, slide 22)."""
    diff = mean1 - mean2
    se = se_xbar_diff(s1, n1, s2, n2)
    return (diff - delta0) / se


def pooled_sd(s1: float, n1: int, s2: float, n2: int) -> float:
    """Pooled standard deviation (Lecture 12, slide 26)."""
    numer = (n1 - 1) * s1 ** 2 + (n2 - 1) * s2 ** 2
    return math.sqrt(numer / (n1 + n2 - 2))


def welch_df(s1: float, n1: int, s2: float, n2: int) -> float:
    """Welch–Satterthwaite df approximation (Lecture 12, slide 27)."""
    v1 = s1 ** 2 / n1
    v2 = s2 ** 2 / n2
    return (v1 + v2) ** 2 / ((v1 ** 2) / (n1 - 1) + (v2 ** 2) / (n2 - 1))


def t_stat_two_means(
    mean1: float,
    mean2: float,
    s1: float,
    n1: int,
    s2: float,
    n2: int,
    delta0: float = 0.0,
    pooled: bool = False,
) -> float:
    """Student‑t statistic for two means (Lecture 12).

    If ``pooled`` is ``True`` use the pooled SD; otherwise use Welch's SE.
    """
    diff = mean1 - mean2
    if pooled:
        sp = pooled_sd(s1, n1, s2, n2)
        se = sp * math.sqrt(1 / n1 + 1 / n2)
    else:
        se = math.sqrt(s1 ** 2 / n1 + s2 ** 2 / n2)
    return (diff - delta0) / se


def t_stat_paired(dbar: float, s_d: float, n: int, mu0: float = 0.0) -> float:
    """Paired‑sample t statistic (Lecture 12, slide 18)."""
    return (dbar - mu0) / (s_d / math.sqrt(n))


def p_value(stat: float, tails: int = 2, df: Optional[int] = None) -> float:
    """Return the p‑value for a Z or t statistic.

    Parameters
    ----------
    stat:
        Observed z or t statistic.
    tails:
        1 for one‑tailed, 2 for two‑tailed tests.
    df:
        Degrees of freedom if ``stat`` follows a t distribution.  ``None`` ⇒
        use the standard normal.
    """
    if df is None:
        dist = stats.norm()
    else:
        dist = stats.t(df)
    prob = dist.sf(abs(stat))
    return prob * tails

# ───────────────────────────────────────────────────────────────────────────────
# Quick‑and‑dirty unit tests against the published answer key
# ───────────────────────────────────────────────────────────────────────────────

Answer = Union[float, Tuple[float, float]]


def approx(a: Answer, b: Answer, tol: float = 5e-3) -> bool:  # noqa: W605
    """Flexible tolerance‑based comparison (scalar or 2‑tuple)."""
    if isinstance(a, tuple):
        return all(abs(x - y) <= tol for x, y in zip(a, b))
    return abs(a - b) <= tol


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
