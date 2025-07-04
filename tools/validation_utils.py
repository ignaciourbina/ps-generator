"""Common statistical helpers for validation pipelines.

Functions mirror the notation used in the lecture slides so validation code
matches the formulas presented in class.
"""

from __future__ import annotations

import math
from statistics import NormalDist
from typing import Tuple

from scipy.stats import t as t_dist

# ---------------------------------------------------------------------------
# Generic helpers
# ---------------------------------------------------------------------------

def margin_of_error(se: float, crit: float) -> float:
    """Return ``crit`` × ``se`` (Lecture 11, slide 6)."""
    return crit * se


def margin_of_error_z(s: float, n: int, z: float = 1.96) -> float:
    """Margin of error for a mean using z procedures."""
    return margin_of_error(s / math.sqrt(n), z)


def p_value(stat: float, two_sided: bool = True, distribution: str = "z", df: int | None = None) -> float:
    """P-value for a z or t statistic."""
    abs_stat = abs(stat)
    if distribution == "z":
        tail = 1 - NormalDist().cdf(abs_stat)
    elif distribution == "t":
        if df is None:
            raise ValueError("df required for t distribution")
        tail = 1 - t_dist.cdf(abs_stat, df)
    else:
        raise ValueError("distribution must be 'z' or 't'")
    return 2 * tail if two_sided else (tail if stat > 0 else 1 - tail)

# ---------------------------------------------------------------------------
# Proportion inference
# ---------------------------------------------------------------------------

def se_hat_p_diff(p1_hat: float, n1: int, p2_hat: float, n2: int) -> float:
    """SE of ``hat p1 - hat p2`` (Lecture 9, slide 12)."""
    return math.sqrt(p1_hat * (1 - p1_hat) / n1 + p2_hat * (1 - p2_hat) / n2)


def pooled_p(x1: int, n1: int, x2: int, n2: int) -> float:
    """Pooled estimator for H0: p1 = p2 (Lecture 9, slide 25)."""
    return (x1 + x2) / (n1 + n2)


def se_pooled_p_diff(x1: int, n1: int, x2: int, n2: int) -> float:
    """SE of ``hat p1 - hat p2`` under H0 (Lecture 9, slide 25)."""
    p_hat = pooled_p(x1, n1, x2, n2)
    return math.sqrt(p_hat * (1 - p_hat) * (1 / n1 + 1 / n2))


def z_stat_two_props(x1: int, n1: int, x2: int, n2: int) -> float:
    """Z statistic for testing ``p1 = p2`` (Lecture 9, slide 24)."""
    p1_hat = x1 / n1
    p2_hat = x2 / n2
    se0 = se_pooled_p_diff(x1, n1, x2, n2)
    return (p1_hat - p2_hat) / se0


def ci_p1_minus_p2(p1_hat: float, n1: int, p2_hat: float, n2: int, z: float = 1.96) -> Tuple[float, float]:
    """Large-sample CI for ``p1 - p2`` (Lecture 9, slide 15)."""
    diff = p1_hat - p2_hat
    se = se_hat_p_diff(p1_hat, n1, p2_hat, n2)
    me = margin_of_error(se, z)
    return diff - me, diff + me

# ---------------------------------------------------------------------------
# Mean inference
# ---------------------------------------------------------------------------

def se_xbar_diff(s1: float, n1: int, s2: float, n2: int) -> float:
    """SE of ``Xbar1 - Xbar2`` (Lecture 10, slide 11)."""
    return math.sqrt(s1 ** 2 / n1 + s2 ** 2 / n2)


def ci_mu1_minus_mu2(mean1: float, mean2: float, s1: float, n1: int, s2: float, n2: int, z: float = 1.96) -> Tuple[float, float]:
    """Large-sample CI for ``mu1 - mu2`` (Lecture 11, slide 12)."""
    diff = mean1 - mean2
    se = se_xbar_diff(s1, n1, s2, n2)
    me = margin_of_error(se, z)
    return diff - me, diff + me


def t_stat_one_mean(xbar: float, mu0: float, s: float, n: int) -> float:
    """Student-t statistic for ``mu = mu0`` (Lecture 12, slide 7)."""
    return (xbar - mu0) / (s / math.sqrt(n))


def t_stat_two_means(mean1: float, mean2: float, s1: float, n1: int, s2: float, n2: int, delta0: float = 0.0) -> float:
    """Welch t statistic for ``mu1 - mu2`` (Lecture 12, slide 27)."""
    se = se_xbar_diff(s1, n1, s2, n2)
    return ((mean1 - mean2) - delta0) / se


def df_paired(n: int) -> int:
    """Degrees of freedom for paired-sample t (Lecture 12, slide 17)."""
    return n - 1


def df_welch(s1: float, n1: int, s2: float, n2: int) -> float:
    """Welch–Satterthwaite df approximation."""
    num = (s1 ** 2 / n1 + s2 ** 2 / n2) ** 2
    den = (s1 ** 4) / (n1 ** 2 * (n1 - 1)) + (s2 ** 4) / (n2 ** 2 * (n2 - 1))
    return num / den


def t_stat_paired(d_bar: float, mu_d0: float, s_d: float, n: int) -> float:
    """t statistic for paired differences."""
    return (d_bar - mu_d0) / (s_d / math.sqrt(n))

# Convenience for self-tests ------------------------------------------------

def approx(a, b, tol: float = 5e-3) -> bool:
    """Return True if ``a`` ≈ ``b`` within ``tol``."""
    if isinstance(a, tuple):
        return all(abs(x - y) <= tol for x, y in zip(a, b))
    return abs(a - b) <= tol
