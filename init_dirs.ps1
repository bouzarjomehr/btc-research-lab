$dirs = @(
"data/raw/binance/spot/BTCUSDT/5m",
"data/processed",
"data/features",
"notebooks",
"src/data",
"src/indicators",
"src/strategies",
"src/backtest",
"src/evaluation",
"reports",
"configs",
"tests",
"docs"
)

foreach ($d in $dirs) {
    New-Item -ItemType Directory -Force -Path $d | Out-Null
}