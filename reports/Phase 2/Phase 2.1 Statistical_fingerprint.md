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