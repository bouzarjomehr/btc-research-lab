from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def get_project_root():
    return PROJECT_ROOT


def get_data_path(*args):
    return PROJECT_ROOT.joinpath("data", *args)


def get_processed_data(file_name: str):
    return PROJECT_ROOT / "data" / "processed" / file_name


def get_raw_data(file_name: str):
    return PROJECT_ROOT / "data" / "raw" / file_name