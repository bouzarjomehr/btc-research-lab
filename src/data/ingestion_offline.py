import zipfile
import pandas as pd
from pathlib import Path

BASE_DIR = Path("data/raw/binance/archive/spot/BTCUSDT/5m/zip files")
OUTPUT_PATH = Path("data/processed/BTCUSDT_5m.parquet")

COLUMNS = [
    "open_time", "open", "high", "low", "close", "volume",
    "close_time", "quote_asset_volume", "number_of_trades",
    "taker_buy_base", "taker_buy_quote", "ignore"
]


def load_from_zip():
    dfs = []

    for zip_file in BASE_DIR.glob("*.zip"):
        with zipfile.ZipFile(zip_file, "r") as z:

            for file in z.namelist():
                if file.endswith(".csv"):
                    with z.open(file) as f:
                        df = pd.read_csv(f, header=None)
                        df.columns = COLUMNS
                        dfs.append(df)

    if not dfs:
        raise ValueError("No CSV files found inside ZIP archives")

    return pd.concat(dfs, ignore_index=True)


def clean(df):
    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")

    for col in ["open", "high", "low", "close", "volume"]:
        df[col] = df[col].astype(float)

    df = df.sort_values("open_time")
    df = df.drop_duplicates("open_time")

    return df[["open_time", "open", "high", "low", "close", "volume"]]


def save(df):
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(OUTPUT_PATH, index=False)


def main():
    print("Loading from ZIP archives...")
    df = load_from_zip()

    print("Cleaning...")
    df = clean(df)

    print("Saving parquet...")
    save(df)

    print("DONE:", OUTPUT_PATH)


if __name__ == "__main__":
    main()