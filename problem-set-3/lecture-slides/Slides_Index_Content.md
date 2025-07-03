# Detailed Slide Index – Week 5 Lectures

> **Note**  Slide numbers follow the original PDF pagination. Citations indicate the lecture file where the content comes from.

---

## Lecture 9 – Inference for Two Proportions (33 slides)

1. **Title Slide** – Course, lecture title, author.
2. **Motivation: Inference for Categorical Differences** – Why compare proportions; policy‑oriented examples.
3. **Introduction to Comparing Proportions** – Practical fields using proportion comparisons.
4. **Example Scenarios** – Medicine, marketing, social‑science cases.
5. **Public‑Opinion Example** – Support for a policy by age group; defines $\hat p_1,\,\hat p_2$.
6. **Psychological‑Experiment Example** – CBT vs MBSR anxiety‑reduction proportions.
7. **Notation & Definitions** – $p_1,\,p_2,\;\hat p_1,\,\hat p_2,\;n_1,\,n_2$.
8. **Statistic of Interest** – Difference $\hat p_1-\hat p_2$; connection to $p_1-p_2$.
9. **Review: Expectation & Variance Rules** – Linearity and independence formulas.
10. **Expectation of $\hat p_1-\hat p_2$** – Unbiased: $E(\hat p_1-\hat p_2)=p_1-p_2$.
11. **Variance of the Statistic** – $\operatorname{Var}(\hat p_1-\hat p_2)=\frac{p_1(1-p_1)}{n_1}+\frac{p_2(1-p_2)}{n_2}$.
12. **Standard Error (SE)** – $SE=\sqrt{\frac{p_1(1-p_1)}{n_1}+\frac{p_2(1-p_2)}{n_2}}$.
13. **Sampling Distribution** – Approx. normal for large samples: $\hat p_1-\hat p_2\sim N( p_1-p_2, SE^2)$.
14. **Derivation Recap** – Uses CLT and independence.
15. **Confidence‑Interval Formula** – $(\hat p_1-\hat p_2)\pm z_{1-\alpha/2}\,SE$.
16. **CI Construction Steps** – Compute $\hat p_i$, SE, critical $z$.
17. **Applied Example – Vaccination Rates (Setup)** – $n_1=400,\hat p_1=0.30;\;n_2=500,\hat p_2=0.25$.
18. **Applied Example (Computation)** – $SE\approx0.032$; 95 % CI $[-0.013,0.113]$.
19. **Interpreting the CI** – Zero inside ⇒ no significant difference.
20. **Common Misconceptions** – CI interpretation cautions.
21. **Section Summary** – Key takeaways for CIs.
22. **Hypothesis‑Testing Intro** – Beyond estimation; test significance.
23. **Formulating Hypotheses** – Null: $p_1-p_2=0$; alternatives.
24. **Test Statistic (z)** – $z=\frac{(\hat p_1-\hat p_2)}{SE_0}$ under $H_0$.
25. **SE Under Null (Pooled)** – $SE_0=\sqrt{\hat p(1-\hat p)(1/n_1+1/n_2)}$, $\hat p=\frac{x_1+x_2}{n_1+n_2}$.
26. **Computing the z‑statistic** – Step‑by‑step recipe.
27. **Decision Rule & p‑value** – Two‑tailed critical region, p‑value formula.
28. **Applied Example (Setup)** – Same vaccination data; hypothesis test.
29. **Applied Example (Calculations)** – $z\approx1.675$, $p\text{-value}\approx0.094$.
30. **Decision & Conclusion** – Fail to reject $H_0$ at 5 %.
31. **Interpretation** – Sampling variability explanation.
32. **Testing Misconceptions** – Errors in reading non‑significant results.
33. **Lecture Summary** – CI & HT workflow for two proportions.

---

## Lecture 10 – Sampling Distributions for Estimators of Continuous Variables (15 slides)

1. **Title Slide** – Lecture information.
2. **Sampling Distribution of $\bar X$** – Concept, mean, variance.
3. **Case 1: Normal Population (Known $\sigma^2$)** – Exact normality; $Z=\frac{\bar X-\mu}{\sigma/\sqrt n}$.
4. **Case 2: Large Sample (CLT)** – Approx. normal regardless of population shape.
5. **Plug‑In Principle** – Replace $\sigma$ with $s$; large‑sample Z‑procedures.
6. **Case 3: Small Sample (Unknown $\sigma^2$)** – Student‑t with $t_{n-1}$.
7. **Why Compare Two Means?** – Business & health examples.
8. **Setup for Two Means** – Independent samples; statistic $\bar X_1-\bar X_2$.
9. **Review of E & Var Rules** – Linearity and independence.
10. **Expectation of the Difference** – Unbiased: $E(\bar X_1-\bar X_2)=\mu_1-\mu_2$.
11. **Variance & SE of Difference** – $SE=\sqrt{\sigma_1^2/n_1+\sigma_2^2/n_2}$.
12. **Sampling Distribution (Large n)** – Approx. normal for $\bar X_1-\bar X_2$.
13. **Plug‑In for Two Means** – Estimate SE with $s_1, s_2$; Z‑statistic.
14. **Small‑Sample Two‑Mean t** – Welch–Satterthwaite df mention.
15. **Summary & Assumptions** – CLT, independence, variance estimation.

---

## Lecture 11 – Large‑Sample Inference for Means (32 slides)

1. **Title Slide** – Lecture details.
2. **Confidence Intervals for Means (Overview)** – Transition from proportions to means.
3. **Central Limit Theorem Recap** – $\bar X\sim N\bigl(\mu,\sigma^2/n\bigr)$ for large $n$.
4. **Unknown $\sigma$: Z‑statistic** – $Z=\frac{\bar X-\mu}{s/\sqrt n}$.
5. **Large‑Sample CI Formula** – $\bar X\pm z_{1-\alpha/2}\,s/\sqrt n$.
6. **Margin of Error** – $ME=z_{1-\alpha/2}\,SE$.
7. **Interpreting a CI** – Correct interpretation language.
8. **Example – Commute Time (Setup)** – $n=100,\bar x=32.5, s=7.0$.
9. **Commute Time (Computation)** – 95 % CI (31.13, 33.87).
10. **Distribution of $\bar X_1-\bar X_2$** – Formula for mean difference.
11. **Unknown Variances (Two Means)** – Estimated SE.
12. **Large‑Sample CI for $\mu_1-\mu_2$** – $(\bar X_1-\bar X_2)\pm z_{1-\alpha/2}SE$.
13. **Interpreting the CI** – Sign of interval.
14. **Example – Study Methods (Setup)** – Scores data.
15. **Study Methods (Calculation)** – 99 % CI (−0.63, 8.03).
16. **Hypothesis‑Testing Intro** – Steps for means.
17. **Example – Hours of Sleep (Setup)** – $n=64$, $\bar x=6.8$.
18. **Hours of Sleep (Calc)** – $Z=-2.67$; reject at 5 %.
19. **Example – Drug Effectiveness (Setup)** – Blood‑pressure drop.
20. **Drug Effectiveness (Calc)** – $Z=2.65$; reject at 1 %.
21. **Non‑zero Null Values** – Motivation.
22. **Adjusted Z Formulas** – One & two means with $\mu_0,\,\Delta_0$.
23. **Example – Calories (Setup)** – $n=49,\bar x=2550$.
24. **Calories (Calc)** – $Z=2.33$; reject at 5 %.
25. **Two‑Means Non‑zero Difference** – Situational examples.
26. **Adjusted Z (Two Means)** – Statistic with $\Delta_0$.
27. **Example – Manufacturing (Setup)** – $\Delta_0=5$.
28. **Manufacturing (Calc)** – $Z=0.43$; fail to reject.
29. **Paired Samples Intro** – Motivation & examples.
30. **Paired CI & Test Formulas** – $\bar d\pm z_{1-\alpha/2}\,s_d/\sqrt n$.
31. **Example – Sleep Intervention** – 95 % CI (0.58, 0.92).
32. **Summary – Formula Cheat‑Sheet** – Table of one‑mean, two‑mean, paired.

---

## Lecture 12 – Small‑Sample Inference for Means: Student‑t (32 slides) 

1. **Title Slide** – Lecture details.
2. **Motivating Example – Tiny Exit Poll** – Need for Student‑t.
3. **What Changes When $n$ Is Small?** – Extra variability; t‑tails.
4. **Checklist for t Methods** – SRS, shape \~ Normal.
5. **Data‑Shape Diagnostics** – Histogram & QQ‑plot guidance.
6. **Intuition Behind QQ‑Plot** – Comparing quantiles.
7. **Sampling Distribution of $\bar X$ (Small n)** – $T=\frac{\bar X-\mu}{s/\sqrt n}\sim t_{n-1}$.
8. **CI Recipe** – $\bar X\pm t^*_{n-1,1-\alpha/2}s/\sqrt n$.
9. **t* vs z*\*\* – Heavier tails ⇒ $t^*>z^*$.
10. **Worked CI Example – Donor Contributions** – 90 % CI (\$39.0, \$46.6).
11. **Five‑Step Hypothesis‑Test Road Map** – H0/Ha, α, statistic, decision, conclusion.
12. **Worked Test Example – Booth Time (Setup)** – $\bar x=7.8, n=12$.
13. **Booth Time (Steps 3‑5)** – $T=2.00<2.201$; fail to reject.
14. **Paired‑Samples Section Intro** – Why pair.
15. **Why Pair?** – Removes between‑subject noise.
16. **Sampling Dist. of Mean Difference** – $T=\frac{\bar d-\mu_d}{s_d/\sqrt n}\sim t_{n-1}$.
17. **Assumptions Recap** – Independence of differences.
18. **CI & Test for $\mu_d$** – Formulae.
19. **Example – Turnout Pre/Post ID Law** – 95 % CI (−3.7, 0.1 pp).
20. **Interpreting the CI** – Plausible range discussion.
21. **Practice Problem** – Paired t test quick calc.
22. **Addendum – Large‑n Paired Difference** – Reverts to Z.
23. **Comparing Two Small Samples Intro** – Independent groups.
24. **Comparing Means (Challenges)** – Two sources of variance.
25. **Why Variance Matters** – Noisy $s_1,s_2$ inflate SE.
26. **Pooling Variances** – Pooled $s_p^2$ & conditions.
27. **Welch t Statistic** – Default unequal‑variance solution.
28. **Pooled vs Welch Decision Tree** – Flowchart.
29. **Example – Civics Quiz Scores (Setup)** – Honors vs Regular.
30. **Civics Quiz (Calculation)** – $T=2.19>2.086$; reject.
31. **Common Traps** – Heteroskedasticity, imbalance, multiple testing.
32. **Key Formulas & Takeaways** – Cheat‑sheet table.

---

### Legend of Symbols

* $\hat p$ = sample proportion · $\bar X$ = sample mean · $s$ = sample SD · $t^*$, $z^*$ = critical values · $SE$ = standard error · $ME$ = margin of error.

---

*End of slide index.*
