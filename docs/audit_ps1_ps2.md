# Audit of Web App Questions for Problem Set 1 and 2

This document captures each question currently present in the self-assessment web apps for Problem Set 1 and Problem Set 2. The goal is to verify their content and map them to curriculum concepts and Bloom levels. The JSON schema referenced is described in [schema.md](schema.md).

## Problem Set 1

### Question 1
*Question*: A survey of 200 social science students revealed that 120 were enrolled in 'Statistics for Social Sciences', 80 in 'Research Methods', and 50 were enrolled in both. What is the probability that a randomly selected student is enrolled in 'Statistics for Social Sciences' but NOT 'Research Methods'?
*Options*: a) `0.25`, b) `0.35`, c) `0.60`, d) `0.40`
*Answer*: b
*Tags*: probability, set-operations
*Bloom*: Apply

### Question 2
*Question*: In a particular city, the probability of rain on any given day is 0.3. What is the probability that it will NOT rain on a given day?
*Options*: a) `0.3`, b) `0.5`, c) `0.7`, d) `1.0`
*Answer*: c
*Tags*: probability, complement-rule
*Bloom*: Apply

### Question 3
*Question*: A university department offers two distinct elective seminars for sociology majors: 'Urban Sociology' and 'Rural Sociology'. A student can only enroll in one. The probability a student chooses 'Urban Sociology' is 0.4, and 'Rural Sociology' is 0.35. What is the probability a student chooses one of these two seminars?
*Options*: a) `0.05`, b) `0.14`, c) `0.75`, d) `1.00`
*Answer*: c
*Tags*: probability, addition-rule
*Bloom*: Apply

### Question 4
*Question*: In a survey of community members, 40% supported a new park (Event A), and 50% supported a library renovation (Event B). 20% supported both initiatives. What is the probability that a randomly selected member supported the park OR the library renovation (or both)?
*Options*: a) `0.90`, b) `0.70`, c) `0.60`, d) `0.20`
*Answer*: b
*Tags*: probability, inclusion-exclusion
*Bloom*: Apply

### Question 5
*Question*: A city has two independent traffic lights. The first traffic light is green with a probability of 0.7. The second traffic light is green with a probability of 0.6. What is the probability that both traffic lights are green when a car approaches them?
*Options*: a) `0.10`, b) `1.30`, c) `0.42`, d) `0.88`
*Answer*: c
*Tags*: probability, independence
*Bloom*: Apply

### Question 6
*Question*: A small committee consists of 4 sociologists and 3 psychologists. Two members are selected at random, one after another without replacement, to lead a discussion. What is the probability that the first selected is a sociologist and the second is a psychologist?
*Options*: a) `12/49`, b) `12/42` or `2/7`, c) `7/12`, d) `1/7`
*Answer*: b
*Tags*: probability, conditional
*Bloom*: Apply

### Question 7
*Question*: The probability that a student passes a research methods exam is 0.8 (Event P). The probability that a student both passes the exam AND completes all homework assignments is 0.72 (Event P ∩ H). Given that a student passed the exam, what is the probability they completed all homework assignments?
*Options*: a) `0.72`, b) `0.80`, c) `0.90`, d) `0.576`
*Answer*: c
*Tags*: conditional-probability
*Bloom*: Apply

### Question 8
*Question*: A study on voting patterns produced the following table for 1000 respondents: ... (table). Given that a randomly selected respondent is from the 18-29 age group, what is the probability that they voted?
*Options*: a) `150/700`, b) `150/1000`, c) `150/250`, d) `250/1000`
*Answer*: c
*Tags*: conditional-probability, contingency-table
*Bloom*: Apply

### Question 9
*Question*: A city's population is 60% urban dwellers and 40% suburban dwellers. 5% of urban dwellers are dissatisfied with public transport, while 10% of suburban dwellers are dissatisfied. What is the overall probability that a randomly selected resident is dissatisfied with public transport?
*Options*: a) `0.075`, b) `0.070`, c) `0.030`, d) `0.040`
*Answer*: b
*Tags*: total-probability
*Bloom*: Apply

### Question 10
*Question*: Referring to the previous question: If a randomly selected resident is dissatisfied with public transport, what is the probability that they are an urban dweller?
*Options*: a) `0.03/0.07 ≈ 0.429`, b) `0.04/0.07 ≈ 0.571`, c) `0.60`, d) `0.05`
*Answer*: a
*Tags*: bayes-theorem
*Bloom*: Apply

### Question 11
*Question*: A student is taking a multiple-choice quiz. For any given question, the student knows the answer with probability 0.6. If they don't know the answer (probability 0.4), they guess randomly from 4 options. What is the probability the student answers a question correctly?
*Options*: a) `0.60`, b) `0.70`, c) `0.25`, d) `0.10`
*Answer*: b
*Tags*: total-probability
*Bloom*: Apply

### Question 12
*Question*: From the previous question: If the student answered a question correctly, what is the probability that they actually knew the answer?
*Options*: a) `0.6/0.7 ≈ 0.857`, b) `0.1/0.7 ≈ 0.143`, c) `0.6`, d) `0.7`
*Answer*: a
*Tags*: bayes-theorem
*Bloom*: Analyze

### Question 13
*Question*: A focus group has 5 women and 3 men. If two people are randomly selected without replacement to give their opinions, what is the probability that both selected are women?
*Options*: a) `25/64`, b) `20/56` or `5/14`, c) `15/56`, d) `5/8`
*Answer*: b
*Tags*: combinatorics, dependent-events
*Bloom*: Apply

### Question 14
*Question*: In a survey, 30% of respondents are aged 18-25. Among the 18-25 age group, 60% use social media platform 'SociConnect'. Among respondents older than 25 (i.e., the other 70%), 40% use 'SociConnect'. If a randomly selected respondent uses 'SociConnect', what's the probability they are in the 18-25 age group?
*Options*: a) `0.18 / 0.46 ≈ 0.391`, b) `0.28 / 0.46 ≈ 0.609`, c) `0.18`, d) `0.46`
*Answer*: a
*Tags*: bayes-theorem, total-probability
*Bloom*: Analyze

## Problem Set 2

### Question 1
*Question*: In statistical inference, an estimator is a rule or formula used to estimate a population parameter based on sample data. Which of the following statements **best describes the property of an unbiased estimator**?
*Options*: a) Expected value equals the true parameter, b) Estimator has zero variance, c) Always yields the exact parameter, d) Sampling distribution is uniform
*Answer*: a
*Tags*: estimators, bias
*Bloom*: Understand

### Question 2
*Question*: Two unbiased estimators A and B estimate the same parameter. If Var(A)=4 and Var(B)=5, which estimator is more efficient?
*Options*: a) Estimator A, b) Estimator B, c) Both equally efficient, d) Cannot determine
*Answer*: a
*Tags*: estimators, efficiency
*Bloom*: Understand

### Question 3
*Question*: According to the Central Limit Theorem, what is the approximate sampling distribution of the sample mean for large n when sampling from a population with mean \( \mu \) and standard deviation \( \sigma \)?
*Options*: a) `N(μ, σ/√n)`, b) `N(0,1)`, c) `N(μ, σ)`, d) Same as original distribution
*Answer*: a
*Tags*: central-limit-theorem
*Bloom*: Understand

### Question 4
*Question*: A random sample of 100 observations has a sample mean of 50 and a sample standard deviation of 10. What is the standard error of the sample mean?
*Options*: a) 10, b) 5, c) 1, d) 0.1
*Answer*: c
*Tags*: standard-error
*Bloom*: Apply

### Question 5
*Question*: Suppose a random sample of 100 observations is taken from a normally distributed population. The sample has a mean of 50 and a sample standard deviation of 10. Based on this information, what is the approximate probability that the sample mean exceeds 52?
*Options*: a) 0.50, b) 0.023, c) 0.977, d) 0.10
*Answer*: b
*Tags*: central-limit-theorem, probability
*Bloom*: Apply

### Question 6
*Question*: A city council commissions a survey of 400 residents, 120 of whom support a proposed policy. What is the **95% confidence interval** for the true proportion that supports the policy?
*Options*: a) `[0.30 ± 0.05]`, b) `[0.255, 0.345]`, c) `[0.230, 0.370]`, d) `[0.295, 0.305]`
*Answer*: b
*Tags*: confidence-interval, proportion
*Bloom*: Apply

### Question 7
*Question*: A national poll surveys 1,000 voters and finds that 48% favor a policy. To test \( H_0: p=0.50 \) versus \( H_a: p \neq 0.50 \), what is the value of the Z test statistic based on the sample?
*Options*: a) -1.27, b) 1.27, c) -2.50, d) 0
*Answer*: a
*Tags*: hypothesis-test, test-statistic
*Bloom*: Apply

### Question 8
*Question*: Based on the test statistic from the previous question and using a 5% significance level, what is the appropriate conclusion regarding public support for the education reform policy?
*Options*: a) Reject H0, b) Fail to reject H0, c) Insufficient information, d) Accept H0
*Answer*: b
*Tags*: hypothesis-test, decision
*Bloom*: Analyze

### Question 9
*Question*: In a recent community survey, 192 out of 400 respondents said they felt safe walking alone at night. Which of the following best represents a **95% confidence interval** for the true proportion of residents who feel safe?
*Options*: a) `[0.43, 0.53]`, b) `[0.48, 0.52]`, c) `[0.44, 0.56]`, d) `[0.40, 0.60]`
*Answer*: a
*Tags*: confidence-interval, proportion
*Bloom*: Apply

### Question 10
*Question*: If a two-sided hypothesis test for a proportion yields a P-value of 0.03, what can you conclude at \(\alpha = 0.05\)?
*Options*: a) Reject H0, b) Fail to reject H0, c) Need a larger sample, d) The parameter equals the null value
*Answer*: a
*Tags*: hypothesis-test, p-value
*Bloom*: Evaluate

### Question 11
*Question*: Which of the following best describes a population parameter?
*Options*: a) Theoretical value describing an entire population, b) Statistic from a sample, c) Random variable from repeated sampling, d) Standard error of an estimator
*Answer*: a
*Tags*: population-parameter
*Bloom*: Understand

### Question 12
*Question*: In hypothesis testing, what does it mean to reject the null hypothesis at the 5% significance level?
*Options*: a) Strong evidence that H0 is true, b) Sufficient statistical evidence to reject H0, c) Probability that H0 is true is exactly 5%, d) Data collected with 5% measurement error
*Answer*: b
*Tags*: hypothesis-test, significance
*Bloom*: Understand

### Question 13
*Question*: Which statement best describes the concept of the standard error (SE) of an estimator in statistical inference?
*Options*: a) Spread of population distribution, b) Standard deviation of the sampling distribution, c) Variance of individual observations, d) Constant regardless of sample size
*Answer*: b
*Tags*: standard-error
*Bloom*: Understand

### Question 14
*Question*: Which of the following is NOT a required condition for the Central Limit Theorem (CLT) to apply to the sampling distribution of the sample mean?
*Options*: a) Independent observations, b) Identically distributed observations, c) Population must be normal, d) Sample size is sufficiently large
*Answer*: c
*Tags*: central-limit-theorem, assumptions
*Bloom*: Understand

### Question 15
*Question*: If \( X_i \sim N(\mu=50, \sigma^2=25) \) and \( n = 46 \), what is the sampling distribution of \( \bar{X} \)?
*Options*: a) `N(50, 25/46)`, b) `N(50, 25)`, c) `Binomial(50, 46)`, d) `Uniform(46, 50)`
*Answer*: a
*Tags*: sampling-distribution
*Bloom*: Understand

### Question 16
*Question*: In hypothesis testing, what is the purpose of the rejection region?
*Options*: a) Range of outcomes unlikely under H0, b) Values most consistent with H0, c) Interval where Ha is accepted, d) Values of the parameter believed most likely
*Answer*: a
*Tags*: hypothesis-test, rejection-region
*Bloom*: Understand

### Question 17
*Question*: In a statistical study with categorical outcomes, how is the sample proportion \(\hat{p}\) calculated from the data?
*Options*: a) Number of successes divided by sample size, b) Sample size divided by number of successes, c) Square root of number of successes, d) Successes minus failures
*Answer*: a
*Tags*: sample-proportion
*Bloom*: Remember

### Question 18
*Question*: What is the variance of the sample proportion \(\hat{p}\)?
*Options*: a) `p(1-p)/n`, b) `p/n`, c) `p(1-p)`, d) `1/n`
*Answer*: a
*Tags*: sample-proportion, variance
*Bloom*: Remember

### Question 19
*Question*: Which Z critical value is used for a 99% confidence interval for a proportion?
*Options*: a) 1.645, b) 1.96, c) 2.576, d) 3.29
*Answer*: c
*Tags*: confidence-interval, z-critical
*Bloom*: Remember

### Question 20
*Question*: Which of the following best describes a correct interpretation of a 95% confidence interval for \(p\)?
*Options*: a) In repeated samples, about 95% of such intervals contain the true \(p\), b) There is a 95% chance that \(p\) equals the sample proportion, c) The probability that \(p\) is inside this interval is 95%, d) 95% of future sample proportions will fall inside the interval
*Answer*: a
*Tags*: confidence-interval, interpretation
*Bloom*: Understand

### Question 21
*Question*: In hypothesis testing, the significance level \( \alpha \) represents:
*Options*: a) Probability of rejecting H0 when it is true, b) Probability that Ha is true, c) Probability that the sample data are correct, d) The P-value of the test
*Answer*: a
*Tags*: hypothesis-test, significance
*Bloom*: Remember

