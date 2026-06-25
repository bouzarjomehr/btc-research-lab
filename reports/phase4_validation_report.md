
# Phase 4 — Validation Report

## Objective

Determine whether H04c represents a deployable trading edge
or a statistical artifact.

---

## Walk-Forward Validation

Results:

2019 -> PF 1.088
2020 -> PF 1.056
2021 -> PF 1.019
2022 -> PF 1.159
2023 -> PF 1.047

Summary:

- OOS PF > 1 in all windows (5/5)
- Worst OOS PF = 1.019

Conclusion:

Edge survives out-of-sample testing.

---

## Bootstrap Monte Carlo

Median Equity : 3.10x

5% Percentile : 0.58x

95% Percentile : 16.34x

P(Equity < 1x) : 13.3%

Conclusion:

Edge appears genuine but relatively weak.

---

## Drawdown Analysis

Worst Historical DD:

-51.3%

Largest Loss:

2020-03-12
Return = -29.7%

Observation:

Drawdowns are concentrated in specific market regimes,
especially March 2020 and the 2022 bear market.

---

## Tail Risk Analysis

Loss <= -5% :

26 trades

11.9% of total losses

Loss <= -10% :

2 trades

Conclusion:

Tail losses are not the primary source of drawdown.

---

## Losing Streak Analysis

Max Losing Streak : 11

Median Losing Streak : 1

95th Percentile : 4

Conclusion:

Extreme losing streaks are not responsible for DD.

---

## Position Sizing

5% Allocation:

Max DD ≈ -3%

10% Allocation:

Max DD ≈ -6%

20% Allocation:

Max DD ≈ -12%

30% Allocation:

Max DD ≈ -17%

Conclusion:

Most drawdown concerns can be mitigated through
conservative position sizing.

---

## Kelly Estimate

Kelly Fraction : 4.86%

Half Kelly : 2.43%

Quarter Kelly : 1.22%

Conclusion:

Optimal sizing is small and consistent with
observed drawdown behaviour.

---

## Final Assessment

H04c survives:

- Transaction Costs
- Walk-Forward Validation
- Bootstrap Monte Carlo

The strategy exhibits:

✓ Persistent out-of-sample edge

✓ Parameter stability

✓ Regime dependence

✓ Practical tradability

Primary weakness:

PF ≈ 1.10

Current status:

VALIDATED EDGE

Suitable for Deployment Research.

END OF PHASE 4 REPORT
