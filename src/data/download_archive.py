import os
import requests
from pathlib import Path
from tqdm import tqdm

SYMBOL = "BTCUSDT"
INTERVAL = "5m"

BASE_URL = (
    "https://data.binance.vision/data/spot/monthly/klines/"
    f"{SYMBOL}/{INTERVAL}/"
)

SAVE_DIR = Path(
    "data/raw/binance/archive/spot/BTCUSDT/5m/zip files"
)

# از اینجا کنترل می‌کنی چند سال دانلود شود
START_YEAR = 2019
END_YEAR = 2024


def build_filename(year, month):
    return f"{SYMBOL}-{INTERVAL}-{year}-{month:02d}.zip"


def download_file(url, path):
    r = requests.get(url, stream=True, timeout=30)

    if r.status_code != 200:
        return False

    with open(path, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)

    return True


def main():
    SAVE_DIR.mkdir(parents=True, exist_ok=True)

    for year in range(START_YEAR, END_YEAR + 1):
        for month in range(1, 13):

            filename = build_filename(year, month)
            url = BASE_URL + filename
            save_path = SAVE_DIR / filename

            if save_path.exists():
                print(f"SKIP (exists): {filename}")
                continue

            print(f"Downloading: {filename}")

            ok = download_file(url, save_path)

            if not ok:
                print(f"NOT FOUND: {filename}")


if __name__ == "__main__":
    main()