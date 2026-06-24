
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
