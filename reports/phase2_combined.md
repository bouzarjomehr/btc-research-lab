

# File: phase 1 Summary.md

# Phase 1 — Data Engineering & Research Lab Setup Summary

## Objective
The goal of Phase 1 was to build a fully reproducible, offline research environment for BTCUSDT market data, eliminating dependency on external APIs and ensuring stable, auditable data for quantitative research.

## 1. Data Source Strategy
Offline-first approach using Binance historical data archives.

- Symbol: BTCUSDT
- Interval: 5-minute candles
- Range: 2019–2024

## 2. Data Acquisition
Monthly ZIP archives downloaded from Binance data repository.

Output:
data/raw/binance/archive/spot/BTCUSDT/5m/zip files/

## 3. Data Ingestion
- Extract ZIP → CSV → unified dataset
- Stored as Parquet

Output:
data/processed/BTCUSDT_5m.parquet

Stats:
- Rows: 630,482
- Columns: 6 (open_time, open, high, low, close, volume)

## 4. Data Quality
- No null values in raw ingestion
- OHLC structure valid
- Minor time gaps detected

## 5. Regularization
Reindexed to full 5-minute timeline.

Output:
data/processed/BTCUSDT_5m_regularized.parquet

Results:
- Original rows: 630,482
- Regularized rows: 631,296
- Missing candles: 814

Fill strategy:
- OHLC: forward fill
- Volume: 0 for missing candles

## 6. Design Principles
- Offline-first architecture
- Reproducibility
- Minimal preprocessing bias
- Explicit time grid enforcement

## 7. Current State
A complete research-ready dataset is now available.

## 8. Next Phase (1.6)
Statistical market structure analysis:
- Returns distribution
- Volatility clustering
- Autocorrelation
- Regime detection
- Hypothesis generation



# File: Phase 2.1 Statistical_fingerprint.md

# Phase 2.1 — Statistical Market Fingerprint (BTCUSDT 5m)

## Objective
Characterize the statistical structure of BTCUSDT 5-minute returns and volatility to identify whether market behavior exhibits exploitable structure.

---

## Dataset
- Source: Binance BTCUSDT 5m candles
- Period: 2019–2024
- Rows: ~631,000
- Preprocessing: forward-filled regularization applied

---

## 1. Returns Distribution Analysis

### Key Results
- Skewness: -0.19
- Kurtosis: 166.65

### Interpretation
- Returns are approximately symmetric (weak negative skew)
- Extremely heavy-tailed distribution (non-Gaussian)

### Implication
- Normality assumption is invalid
- Risk is dominated by rare extreme events rather than typical fluctuations

---

## 2. Volatility Structure

### Observations
- Strong volatility clustering observed
- Clear regime-like spikes in rolling volatility
- Max volatility ≈ 17× median level

### Summary Statistics
- Mean volatility: ~0.00174
- Std: ~0.00128
- Max: ~0.0293

### Interpretation
- Volatility is state-dependent (non-IID)
- Market alternates between low and high volatility regimes

---

## 3. Market Structure Insight

The BTCUSDT market exhibits:

1. Non-Gaussian return distribution
2. Heavy-tailed risk profile
3. Strong volatility clustering
4. Evidence of latent regime switching behavior

---

## 4. Implications for Modeling

- IID assumptions are invalid
- Linear predictive models on returns are unlikely to succeed
- Volatility regime modeling is a primary candidate for signal extraction

---

## 5. Conclusion

BTCUSDT 5m market structure is regime-driven rather than stationary.
This justifies moving toward regime detection and conditional strategy design.

---

## Next Step (Phase 2.2)
- Volatility-based regime labeling
- Transition dynamics analysis
- Memory structure of volatility regimes


# File: Phase 2.2–2.4 — Volatility Regime Detection & Return Analysis.docx

Phase 2.2–2.3 — Volatility Regime Detection & Regime-Conditioned Return Analysis
Objective
Investigate whether BTCUSDT 5-minute volatility exhibits persistent regime structure and determine whether volatility regimes contain predictive information about future returns.
Dataset
Asset: BTCUSDT
Timeframe: 5 minutes
Period: 2019–2024
Observations: ~631,000
Methodology
Volatility Proxy
Realized Volatility (RV):
RV_t = Sum of squared returns over rolling window
Parameters:
Rolling window: 48 candles (~4 hours)
Smoothing: EWMA (span = 10)
Regime Construction
Quantile-based discretization:
Regime 0: Low Volatility
Regime 1: Medium Volatility
Regime 2: High Volatility
Regime frequencies:
Low: 33.3%
Medium: 33.3%
High: 33.3%
Transition Matrix
Shuffled Baseline
Findings
Regime Persistence
Probability of remaining in same regime:
Low Volatility: 99.03%
Medium Volatility: 98.05%
High Volatility: 99.02%
Conclusion:
Volatility regimes exhibit extremely strong temporal persistence.
Randomness Test
Comparison with shuffled baseline demonstrates that the observed regime structure is not an artifact of random ordering.
Conclusion:
Volatility regimes represent genuine temporal structure in BTC market dynamics.
Return Distribution by Regime
Observation:
Return variance increases substantially across volatility regimes.
Tail Behavior
1% Quantile:
Low: -0.247%
Medium: -0.419%
High: -0.865%
99% Quantile:
Low: +0.250%
Medium: +0.414%
High: +0.856%
Observation:
High-volatility regimes produce substantially larger price moves in both directions.
Future Return Analysis
Mean next-candle return:
Conclusion:
Volatility regimes affect:
Variance 
Tail magnitude
Volatility regimes do not provide meaningful directional forecasting power.
Research Conclusions
Supported:
BTC volatility exhibits strong regime behavior.
Regimes possess substantial persistence.
Volatility regimes are statistically real and non-random.
Regimes explain future volatility conditions.
Rejected:
Volatility regimes alone predict future return direction.
Volatility regimes alone provide a directional trading edge.
Implication for Strategy Research
Volatility regimes appear useful for:
Risk management
Position sizing
Strategy conditioning
Volatility regimes do not appear sufficient as standalone entry signals.
Phase 2.4 — Return Dependence Analysis
Objective
Determine whether BTC 5m returns contain exploitable directional memory.
Autocorrelation of Returns
Results
Lag-1:
-0.032
Higher lags:
Approximately zero.
Interpretation
Returns exhibit almost no serial dependence.
Direction behaves close to random.
Autocorrelation of Absolute Returns
Results
Lag-1:
0.389
Lag-20:
0.228
Interpretation
Strong and slowly decaying memory exists in return magnitude.
Volatility clustering is highly persistent.
Autocorrelation of Squared Returns
Results
Lag-1:
0.253
Lag-20:
0.038
Interpretation
Volatility exhibits persistent but decaying dependence.
This behavior is consistent with heteroskedastic processes and GARCH-type dynamics.
Integrated Interpretation
BTCUSDT 5m exhibits:
Direction
Nearly memoryless.
Simple momentum and mean-reversion effects are weak or absent.
Volatility
Highly structured and persistent.
Volatility possesses regime behavior and long memory.
Main Research Conclusions
Supported:
✓ Heavy-tailed return distribution.
✓ Strong volatility clustering.
✓ Persistent volatility regimes.
✓ Regime structure is non-random.
✓ Absolute and squared returns exhibit long memory.
✓ Future volatility is partially predictable.
Rejected:
✗ IID assumptions.
✗ Gaussian assumptions.
✗ Volatility regime as a directional predictor.
✗ Significant autocorrelation in returns.
✗ Simple momentum/mean-reversion as a source of edge.
Overall Conclusion of Phase 2.1–2.4
BTCUSDT 5m behaves as a process with:
Memoryless direction + memoryful volatility
The market appears more predictable in terms of risk and volatility than in terms of price direction.
Next Phase
Phase 2.5 — Conditional Structure Analysis
Research Question:
Does market structure depend on volatility regime?
Topics:
ACF of returns by regime. 
ACF of absolute returns by regime. 
Tail behavior by regime. 
Transition-conditioned returns. 
Search for regime-specific edge. 
Current State of the Project
No evidence yet supports a directional trading edge.
However, strong evidence supports:
volatility-aware models, 
regime-conditioned strategies, 
and conditional rather than unconditional market structure. 


# File: Phase 2.5 Conditional Structure Analysis.docx

Phase 2.5 — Conditional Structure Analysis
Objective
Investigate whether statistical structure in BTCUSDT 5-minute returns is regime-dependent and identify potential conditional edges.
Phase 2.5.1 — ACF by Volatility Regime
Result
Return autocorrelation is slightly negative in all volatility regimes.
Lag-1 autocorrelation:
Low Vol: -0.0297
Mid Vol: -0.0201
High Vol: -0.0375
The strongest anti-persistence appears in High Vol regimes.
Phase 2.5.2 — Multi-Lag Mean Reversion
Sign reversal probabilities:
Low Vol
Lag1: 51.7%
Lag2: 51.3%
Lag3: 50.8%
Mid Vol
Lag1: 52.2%
Lag2: 51.4%
Lag3: 50.7%
High Vol
Lag1: 52.3%
Lag2: 51.7%
Lag3: 50.6%
Mean reversion persists beyond Lag1 but decays rapidly.
Phase 2.5.3–2.5.4 — Transition Analysis
Transitions between volatility regimes show little evidence of persistent directional edge.
Some weak effects were observed during volatility expansion, but most disappeared at longer horizons.
Conclusion:
No robust transition-based edge was detected.
Phase 2.5.5 — Asymmetry Analysis
Large negative returns are followed by positive future returns.
Large positive returns are followed by mild negative future returns.
Mean reversion exists and persists up to 6 bars.
Phase 2.5.6 — Magnitude Dependence
Larger shocks tend to produce stronger subsequent reversals.
The strongest effects are concentrated in the largest return observations.
Phase 2.5.7 — Extreme Positive vs Extreme Negative Shocks
Extreme positive shocks showed little evidence of predictable reversal.
Extreme negative shocks displayed statistically significant positive mean reversion.
This revealed clear asymmetry.
Phase 2.5.8 — Regime-conditioned Extreme Negative Shocks
Among 6313 extreme negative shocks:
Low Vol: 126
Mid Vol: 823
High Vol: 5364
Strong positive mean reversion was almost entirely concentrated in High Vol regimes.
High Vol + Extreme Negative Shock:
FWD6 ≈ +0.155%
Phase 2.5.9 — Distribution Robustness
Subset:
Extreme Negative Shock (1%)
High Vol Regime
Sample size:
5364 observations
Results:
Mean FWD6 = +0.155%
Median FWD6 = +0.193%
Hit Rate = 57.6%
t-stat = 6.87
Median exceeded mean, indicating that the effect is not driven by a few outliers.
Main Conclusions
BTCUSDT 5-minute returns are not perfectly memoryless.
Volatility clustering is strong.
Short-term mean reversion exists.
Mean reversion is asymmetric.
The strongest reversals occur after extreme negative shocks.
These reversals are concentrated in high-volatility regimes.
Hypothesis H-01
In BTCUSDT 5-minute data, extreme negative shocks occurring during high-volatility regimes are followed by statistically significant positive mean reversion over the next ~30 minutes.
Characteristics:
~5364 observations
Mean FWD6 ≈ +0.155%
Median FWD6 ≈ +0.193%
Hit Rate ≈ 57.6%
t-stat ≈ 6.87
H-01 is the first statistically robust conditional hypothesis identified by the BTC Research Lab.
Future validation:
Macro regime segmentation (Bull / Bear / Sideways)
Time stability analysis
Out-of-sample testing
Transaction cost analysis
Walk-forward validation


# File: Phase 2.6 — Macro Regime Segmentation.docx

Phase 2.6 — Macro Regime Segmentation
Objective
Evaluate whether H-01 is stable across macro market regimes.
Macro Regime Definition
Bull market: Daily Close > Daily MA200
Bear market: Daily Close ≤ Daily MA200
H-01 Definition
Extreme Negative Shock (bottom 1% of returns)
Highest Volatility Regime (regime = 2)
Prediction horizon:
FWD6 (≈30 minutes)
Sample Size
Total H-01 observations: 5364
Bull market observations: 2415
Bear market observations: 2949
Results
Bull Market
Mean FWD6 = +0.2005%
Median FWD6 = +0.2544%
Hit Rate = 59.5%
t-stat = 7.15
p-value = 1.14×10⁻¹²
Bear Market
Mean FWD6 = +0.1183%
Median FWD6 = +0.1476%
Hit Rate = 56.1%
t-stat = 3.47
p-value = 5.36×10⁻⁴
Direct Comparison
Difference in mean FWD6:
0.0822%
Welch t-stat:
1.86
Welch p-value:
0.063
Conclusions
H-01 exists in both Bull and Bear markets.
Positive mean reversion remains statistically significant in both regimes.
The effect appears stronger during Bull markets.
However, the difference between Bull and Bear regimes is not statistically significant at the 5% level.
Therefore, current evidence suggests that H-01 is likely a structural feature of BTC market behavior rather than a phenomenon specific to one market cycle.
Updated Hypothesis
H-01:
Extreme negative shocks occurring during the highest volatility regime are followed by statistically significant positive mean reversion over the next approximately 30 minutes.
This effect is observed in both Bull and Bear markets and appears to be structurally persistent.


# File: Phase 2.7 — Temporal Robustness Analysis.docx

Phase 2.7 — Temporal Robustness Analysis
Objective
Evaluate whether H-01 is stable across different temporal dimensions and determine whether the observed edge represents a structural characteristic of Bitcoin market behavior or merely a historical artifact.
H-01 Definition
Extreme Negative Shock (bottom 1% of returns)
Highest Volatility Regime (regime = 2)
Prediction Horizon:
FWD6 (≈30 minutes)
Phase 2.7a — Intraday Session Stability
Session Definitions
Asia: 00:00–08:00 UTC
Europe: 08:00–16:00 UTC
US: 16:00–24:00 UTC
Results
Asia
n = 1389
Mean FWD6 = +0.1521%
Hit Rate = 56.4%
p-value = 0.0032
Europe
n = 1882
Mean FWD6 = +0.1684%
Hit Rate = 57.2%
p-value = 4.70×10⁻⁶
US
n = 2093
Mean FWD6 = +0.1457%
Hit Rate = 58.7%
p-value = 1.26×10⁻⁵
ANOVA:
p-value = 0.908
Conclusion
No statistically significant differences were observed among major trading sessions.
Phase 2.7b — Yearly Stability
ANOVA:
p-value = 0.0029
Conclusion
The strength of H-01 varied across years.
Phase 2.7c — Macro Cycle Stability
Cycle Definitions
Pre-Covid
Covid Bull
Bear Market
ETF Era
ANOVA:
p-value = 0.0147
Conclusion
H-01 is regime dependent and exhibits different strengths across macro market cycles.
Phase 2.7d — Rolling Stability
12-month rolling window with 3-month step.
Findings
Weak edge during 2019–early 2020.
Strong plateau during 2020–2021.
Gradual weakening throughout 2022.
Partial recovery during 2023–2024.
The changes were continuous rather than abrupt, indicating that regime effects are not artifacts of arbitrary calendar boundaries.
Phase 2.7e — Volatility-Normalized Analysis
Normalized Return:
norm_fwd_6 = fwd_6 / rolling_vol
Findings
The temporal pattern observed in raw returns remained largely unchanged after volatility normalization.
Conclusion
Changes in H-01 strength cannot be explained solely by changes in market volatility.
Phase 2.7f — Chronological Out-of-Sample Test
Train Set
2019–2022
n = 3751
Mean FWD6 = +0.163%
Hit Rate = 57.0%
p-value = 6.86×10⁻⁸
Test Set
2023–2024
n = 415
Mean FWD6 = +0.128%
Hit Rate = 59.3%
p-value = 0.028
Shock threshold learned from Train:
-0.6525%
Conclusion
H-01 remained statistically significant out-of-sample without parameter adjustment.
Overall Conclusions
H-01 is stable across major trading sessions.
The strength of H-01 varies over time and across macro market regimes.
Temporal differences are not solely explained by changes in volatility.
Rolling-window analysis suggests gradual regime-dependent variations rather than abrupt structural breaks.
Out-of-sample testing confirms that H-01 is not merely a historical artifact.
Updated Hypothesis
Extreme negative shocks occurring during the highest volatility regime are followed by statistically significant positive mean reversion over approximately the next 30 minutes.
The strength of this effect varies across market regimes, but the phenomenon persists out-of-sample and therefore appears to represent a genuine and potentially exploitable statistical feature of Bitcoin market behavior.


# File: phase 2_h01_summary.md


Phase 2.7–2.18 Summary: H-01 Shock-Based Strategy Research

1. Objective
Investigate whether extreme negative shocks in high-volatility regimes (H-01) produce a tradable edge in BTCUSDT.

2. Key Findings

Phase 2.7 – Temporal Robustness
- Signal stable across sessions
- Regime-dependent across years and macro cycles

Phase 2.8 – Horizon Analysis
- Weak delayed drift observed (best at longer horizons)
- Non-monotonic behavior

Phase 2.12 / 2.16 – Backtesting
- Initial backtest Sharpe: negative (~ -0.48)
- Filtered analysis showed positive drift but selection bias present

Phase 2.17 – Regime Decomposition
- Three regimes identified:
  * Low volatility: noise-dominated
  * Medium volatility: weak drift
  * High volatility: strongest signal (~0.56 hit rate, small positive mean)

Phase 2.18 – Cluster-Based Strategy
- Clustered shocks showed strongest raw statistics:
  * Mean ≈ 0.00425
  * Hit rate ≈ 0.61
- However, full execution backtest:
  * Sharpe ≈ -0.24
  * Negative expectancy after costs and structure

3. Final Conclusion

- H-01 is NOT a tradable alpha signal
- It is a conditional distribution-shift indicator
- Predictive power exists in aggregate but not in executable paths

4. Structural Insight

Market behavior:
- Shock events shift return distribution
- They do NOT provide directional predictability
- Edge collapses under realistic execution constraints

5. Implication

- Remove H-01 from strategy layer
- Use only as risk/regime overlay feature
- Proceed to transition-based alpha discovery (Phase 3)

END OF PHASE 2 REPORT
