# H04c Specification v1.1

Generated:
2026-06-25 UTC

---

Strategy Name

H04c

Status

VALIDATED EDGE

---

Market

BTCUSDT Spot

Execution Model

Event-Based

---

Dataset

Source:
BTCUSDT 5m

Reference File:
data/processed/BTCUSDT_5m_regularized.parquet

Sample Period:
2019-01-01 → 2024-12-31

---

Pattern

DDD

Definition

ret[t]   < 0

ret[t-1] < 0

ret[t-2] < 0

---

Strength

ddd_strength =
ret[t]

* ret[t-1]
* ret[t-2]

Threshold

Q10 of DDD sample

Observed Threshold

-0.007527

---

Direction

Long Only

---

Entry Conditions

1. Pattern == DDD

2. ddd_strength <= Q10 threshold

---

Holding Period

36 bars

(3 hours)

---

Transaction Cost

4 bp round-trip

---

Position Overlap

Not Allowed

---

Stop Loss

None

---

Leverage

None

---

Output Files

Signals:

data/signals/h04c_signals.parquet

Executable Signals:

data/signals/h04c_executable_signals.parquet

Trades:

data/backtests/h04c_trades.parquet

---

Validation Results

Trades:

2840

Mean Return:

0.058%

Hit Rate:

54.9%

Profit Factor:

1.097

Sharpe:

1.63

Max Drawdown:

-51.3%

Final Equity:

3.07x

---

Walk-Forward Validation

2019 -> PF 1.088

2020 -> PF 1.056

2021 -> PF 1.019

2022 -> PF 1.159

2023 -> PF 1.047

Result:

PASS

---

Monte Carlo Validation

Median Equity:

3.10x

5% Percentile:

0.58x

Probability(Equity < 1):

13.3%

Result:

PASS

---

Phase 5 Reconstruction Check

Raw Signals:

6990

Executable Trades:

2839

Historical Trade File:

2840

Result:

PASSED RECONSTRUCTION

---

Current Status

READY FOR PAPER TRADING

READY FOR DEPLOYMENT RESEARCH

---
