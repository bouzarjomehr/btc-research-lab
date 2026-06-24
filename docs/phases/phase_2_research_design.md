# Phase 2 — Statistical Market Structure Analysis

## Objective
Identify statistically robust and repeatable structures in BTCUSDT price behavior.

## Data Source
- BTCUSDT 5m regularized dataset (Phase 1)

## Planned Analyses
- Returns distribution (log returns preferred)
- Volatility clustering (rolling std, GARCH baseline optional later)
- Autocorrelation structure (ACF/PACF)
- Regime detection (initial unsupervised heuristics)
- Microstructure bias checks

## Output
- List of validated statistical phenomena
- Hypothesis candidates for strategy design

## Constraints
- No trading logic yet
- No indicators unless justified by statistics
- Focus on descriptive + inferential structure