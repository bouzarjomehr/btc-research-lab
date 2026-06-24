import requests
import pandas as pd
import os

SYMBOL = "BTCUSDT"
INTERVAL = "5m"
START_TIME = "1 Jan, 2018"

BASE_URL = "https://api.binance.com/api/v3/klines"

SAVE_PATH = "data/raw/binance/spot/BTCUSDT/5m/BTCUSDT_5m.parquet"


def fetch_klines():
    params = {
        "symbol": SYMBOL,
        "interval": INTERVAL,
        "startTime": None
    }

    all_data = []
    limit = 1000
    start_time = None

    while True:
        if start_time:
            params["startTime"] = start_time

        params["limit"] = limit

        resp = requests.get(BASE_URL, params=params, timeout=10)

        if resp.status_code != 200:
            print(resp.text)
            break

        data = resp.json()

        if not data:
            break

        all_data.extend(data)

        start_time = data[-1][0] + 1

        if len(data) < limit:
            break

    return all_data


def process(data):
    df = pd.DataFrame(data, columns=[
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base", "taker_buy_quote", "ignore"
    ])

    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")

    for col in ["open", "high", "low", "close", "volume"]:
        df[col] = df[col].astype(float)

    return df[["open_time", "open", "high", "low", "close", "volume"]]


def save(df):
    os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
    df.to_parquet(SAVE_PATH, index=False)


def main():
    data = fetch_klines()
    df = process(data)
    save(df)
    print("Saved:", SAVE_PATH)


if __name__ == "__main__":
    main()