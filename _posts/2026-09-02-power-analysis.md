---
layout: post
title: "Power Analysis: Plan Before You Run"
date: 2026-09-02 10:00:00 -0700
description: "A practical starting point for choosing a sample size before an experiment begins."
categories: [experimentation, statistics]
---

## Introduction {#introduction}

Power analysis is the habit of deciding what evidence would be useful *before* collecting data. It turns a vague question—“how many observations do we need?”—into a few explicit assumptions: the smallest effect worth detecting, the acceptable false-positive rate, and the chance of detecting that effect.

For an A/B test, the practical output is usually a sample size per group. The answer is never universal: smaller effects need more data, and demanding higher confidence costs more observations.

## Statistical background {#statistical-background}

For a two-sided test, set a significance level `alpha` (often 0.05). Statistical power is `1 - beta`: the probability that the test detects a real effect of the size we planned for. A common target is 80% power, which means accepting a 20% chance of missing that effect.

The standardized effect size, Cohen's *d*, expresses the difference in standard-deviation units. For two equally sized groups, a useful normal-approximation planning formula is:

```text
n per group ≈ 2 × (z(1 - alpha/2) + z(power))² / d²
```

It is a planning approximation, not a substitute for checking the assumptions of the final analysis.

## A small calculation {#a-small-calculation}

The following Python function computes approximate power for a two-sided test with two equally sized groups.

```python
from statistics import NormalDist

normal = NormalDist()

def approximate_power(n_per_group, effect_size, alpha=0.05):
    critical = normal.inv_cdf(1 - alpha / 2)
    signal = effect_size * (n_per_group / 2) ** 0.5
    return normal.cdf(-critical - signal) + 1 - normal.cdf(critical - signal)

print(f"{approximate_power(130, 0.35):.1%}")
# 80.1%
```

The exact sample size should be rounded up and then adjusted for expected attrition, clustering, repeated looks, or any design detail that reduces the information in a raw row count.

## Reading the curves {#reading-the-curves}

The first figure shows how quickly power rises as each group grows. With a modest effect (`d = 0.35`), the curve reaches roughly 80% around 130 observations per group. A small effect requires far more data; a large effect reaches useful power much sooner.

![Power curves for three standardized effect sizes]({{ '/assets/images/power-analysis-power-curves.svg' | relative_url }})

Holding the effect size fixed makes the trade-off even clearer. The second figure uses `d = 0.35` and asks how much power we want to buy. Moving from 80% to 90% is a meaningful increase in reliability—and a meaningful increase in sample size.

![Required sample size by desired power]({{ '/assets/images/power-analysis-sample-size.svg' | relative_url }})

## Conclusion {#conclusion}

The useful question is not “what sample size is standard?” It is: *what effect would change a decision, and how likely do we need to be to notice it?* Put those choices in writing before the data arrives; then the sample-size calculation becomes an auditable design decision instead of a post-hoc justification.
