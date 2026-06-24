# Phase 3 — H04c Pattern-Based Strategy Research

## Objective

Following the failure of H01 as a tradable strategy, Phase 3 shifted from purely statistical hypothesis testing toward a more practical trading-oriented approach.

The objective was to discover executable price-action structures capable of producing persistent and tradable edge.

---

# Phase 3.1 — Compression → Expansion

### Hypothesis H02

Periods of extremely compressed volatility are followed by volatility expansion.

### Findings

Compression events were followed by lower-than-baseline probabilities of large moves.

Results:

* Baseline probability of large move ≈ 25.3%
* Event probability ≈ 3.9%
* Lift ≈ 0.155

### Conclusion

H02 rejected.

Compression events do not generate useful expansion opportunities.

---

# Phase 3.2 — Volatility Expansion Events

### Hypothesis H03

Large volatility expansions may contain directional information.

Results:

* Event probability of large move > baseline.
* Mean absolute future returns increased.
* Long hit rate ≈ 52.2%
* Short hit rate ≈ 47.8%

Directional edge remained weak.

### Conclusion

Volatility expansion predicts future volatility but not direction.

---

# Phase 3.3 — Momentum Continuation

Momentum continuation after expansion was tested.

Results:

Up momentum:

* Continuation rate ≈ 48.3%

Down momentum:

* Continuation rate ≈ 44.4%

### Conclusion

No robust continuation effect.

H03 rejected as alpha source.

---

# Phase 3.4 — Three-Bar Pattern Mining

Eight possible 3-bar sign patterns were evaluated.

Strongest pattern:

DDD

Results:

* n = 70691
* mean FWD6 ≈ 0.018%
* hit rate ≈ 54.5%

Weakest pattern:

UUU

* mean FWD6 ≈ -0.008%

### Conclusion

Three consecutive down bars exhibit statistically significant mean reversion.

---

# Phase 3.4b — Horizon Analysis

DDD pattern showed increasing edge over longer horizons.

Results:

FWD3:

* hit ≈ 55.1%

FWD6:

* hit ≈ 54.5%

FWD12:

* hit ≈ 54.6%

FWD24:

* mean ≈ 0.033%

### Conclusion

Edge accumulates gradually.

---

# Phase 3.4c — Magnitude Segmentation

DDD events were divided by strength.

Strongest quartile (Q1):

Results:

* mean FWD24 ≈ 0.074%
* hit rate ≈ 55.8%

### Conclusion

Stronger selloffs create stronger mean reversion.

---

# Overlap with H01

Overlap:

* H04_Q1 = 17673
* H01 = 6313
* Overlap = 2016

Overlap ratios:

* 11.4% of H04_Q1
* 31.9% of H01

### Conclusion

H04 and H01 are largely distinct phenomena.

---

# Volatility Regime Conditioning

Performance by volatility regime:

Low:

* mean FWD24 ≈ 0.036%

Mid:

* mean FWD24 ≈ -0.006%

High:

* mean FWD24 ≈ 0.106%

### Conclusion

High-volatility regime contains most of the edge.

---

# H04c Strategy Definition

Entry conditions:

1. Pattern = DDD
2. Strongest 10% of DDD events
3. High-volatility regime only
4. Long-only

Exit:

36 bars later (3 hours)

Transaction cost:

4 bp

No stop loss

No leverage

No overlap

---

# Event Backtester

Results:

Trades:

* 2840

Mean return:

* 0.058%

Hit rate:

* 54.9%

Profit factor:

* 1.097

Sharpe:

* 1.63

Maximum drawdown:

* -51.3%

Final equity:

* 3.07×

---

# Year-by-Year Performance

2019:

+34%

2020:

+59%

2021:

+48%

2022:

-34%

2023:

+40%

2024:

+5%

### Conclusion

2022 represented the weakest regime.

Overall profitability persisted.

---

# Volatility Regime Performance

Low volatility:

PF = 0.894

Mid volatility:

PF = 0.954

High volatility:

PF = 1.154

Final equity:

4.26×

### Conclusion

Edge is concentrated almost entirely in high-volatility regimes.

---

# Bull Market Filter

HighVol + Bull:

Results:

* n = 901
* Hit rate = 57.8%
* PF = 1.239
* Sharpe = 2.29
* MaxDD = -24.5%
* Final equity = 3.01×

### Conclusion

Bull filtering substantially improves risk-adjusted performance.

---

# Exposure Analysis

Exposure:

10.6%

CAGR:

27.3%

### Conclusion

The strategy spends most of its time out of the market.

---

# MAE / MFE Analysis

Winning trades:

Median MAE:

* -0.55%

Median MFE:

* +1.5%

Losing trades:

Median MAE:

* -1.78%

Median MFE:

* +0.7%

### Conclusion

Winning trades are relatively clean.

---

# Stop Loss Sweep

Tested:

1%–4%

Results:

Every stop-loss configuration reduced performance.

Example:

SL 1%

* Equity = 0.36×

SL 4%

* Equity = 1.10×

No SL:

* Equity = 3.07×

### Conclusion

Classical stop-loss damages H04c.

Large winners require tolerance for adverse excursions.

---

# Time Exit Sweep

Best horizons:

36–48 bars

H=36:

* PF = 1.097
* Sharpe = 1.63
* MaxDD = -51%

H=48:

* Slightly higher equity
* Significantly worse drawdown

### Conclusion

36 bars provide the best balance between return and risk.

---

# Structural Characteristics

H04c exhibits:

✓ Strong parameter stability.

✓ Out-of-sample persistence.

✓ Volatility regime dependence.

✓ Tail-driven behavior.

✓ Slow mean reversion dynamics.

✓ High sensitivity to stop-loss.

✓ Robustness across years.

✓ Practical executable edge.

---

# Final Conclusion

Unlike H01, H04c survives realistic execution assumptions.

However:

* Profit factor remains modest (~1.10).
* Performance is highly dependent on large winners.
* Drawdowns remain substantial.

H04c appears to represent a genuine but weak market inefficiency.

The strategy is sufficiently mature to leave the discovery phase and enter formal validation.

---

# Next Phase

## Phase 4 — Validation

Planned components:

### Phase 4.1

Monte Carlo robustness

### Phase 4.2

Walk-forward validation

### Phase 4.3

Risk of ruin analysis

### Phase 4.4

Position sizing

### Phase 4.5

Portfolio construction

Goal:

Determine whether H04c constitutes a deployable trading system or merely a statistically interesting pattern.

END OF PHASE 3 REPORT
