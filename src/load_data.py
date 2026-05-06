import pandas as pd
from pathlib import Path
from typing import Dict, Tuple

from config import RAW_FILES


def load_csv(file_path: Path) -> pd.DataFrame:
    """
    Load CSV with optimizations for large files (especially studentVle).
    """
    print(f"Loading {file_path.name}...")

    if not file_path.exists():
        raise FileNotFoundError(f"Missing file: {file_path}")

    # Special handling for large file
    if file_path.name == "studentVle.csv":
        df = pd.read_csv(
            file_path,
            usecols=[
                "code_module",
                "code_presentation",
                "id_student",
                "date",
                "sum_click",
            ],
            dtype={
                "code_module": "category",
                "code_presentation": "category",
                "id_student": "int32",
                "date": "int16",
                "sum_click": "int32",
            }
        )
        return df

    # Default loading for other files
    return pd.read_csv(file_path)


def load_oulad_data() -> Dict[str, pd.DataFrame]:
    """
    Load all OULAD datasets into a dictionary.
    """
    data = {}

    for name, path in RAW_FILES.items():
        df = load_csv(path)
        print(f"{name} loaded with shape: {df.shape}")
        data[name] = df

    return data


def basic_checks(data: Dict[str, pd.DataFrame]) -> Dict[str, Tuple[int, int]]:
    """
    Return shapes of all datasets.
    """
    summary = {}
    for name, df in data.items():
        summary[name] = df.shape
    return summary


def preview_columns(data: Dict[str, pd.DataFrame]):
    """
    Print column names of each dataset (useful for debugging).
    """
    print("\nColumn Preview:")
    for name, df in data.items():
        print(f"\n{name}:")
        print(list(df.columns))


if __name__ == "__main__":
    data = load_oulad_data()

    print("\nDataset Shapes:")
    for name, shape in basic_checks(data).items():
        print(f"{name}: {shape}")

    preview_columns(data)