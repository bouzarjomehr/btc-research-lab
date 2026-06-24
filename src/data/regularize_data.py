import pandas as pd

INPUT_PATH = "data/processed/BTCUSDT_5m.parquet"
OUTPUT_PATH = "data/processed/BTCUSDT_5m_regularized.parquet"


def load_data():
    df = pd.read_parquet(INPUT_PATH)
    df["open_time"] = pd.to_datetime(df["open_time"])
    return df


def regularize(df):
    df = df.sort_values("open_time")
    df = df.set_index("open_time")

    # ساخت timeline کامل 5-minute
    full_index = pd.date_range(
        start=df.index.min(),
        end=df.index.max(),
        freq="5min"
    )

    df = df.reindex(full_index)

    df.index.name = "open_time"

    return df


def handle_missing(df):
    missing_count = df["close"].isna().sum()
    print(f"Missing candles after reindex: {missing_count}")

    # فعلاً conservative approach:
    # فقط price را forward fill می‌کنیم
    price_cols = ["open", "high", "low", "close"]

    df[price_cols] = df[price_cols].ffill()

    # volume برای missing ها = 0
    df["volume"] = df["volume"].fillna(0)

    return df


def save(df):
    df = df.reset_index()
    df.to_parquet(OUTPUT_PATH, index=False)


def main():
    df = load_data()

    print("Original shape:", df.shape)

    df = regularize(df)

    print("After regularization:", df.shape)

    df = handle_missing(df)

    save(df)

    print("Saved:", OUTPUT_PATH)


if __name__ == "__main__":
    main()