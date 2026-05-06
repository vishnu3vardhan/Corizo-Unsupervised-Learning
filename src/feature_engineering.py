import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

from config import CLEANED_FILE, ENGINEERED_FILE


def create_engagement_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add behavior-focused features.
    """
    out = df.copy()

    # Timing-based features
    out["activity_span"] = out["last_activity_day"] - out["first_activity_day"]
    out["activity_span"] = out["activity_span"].fillna(0)

    out["clicks_per_course_day"] = out["total_clicks"] / (out["activity_span"] + 1)
    out["clicks_per_course_day"] = out["clicks_per_course_day"].replace([np.inf, -np.inf], np.nan).fillna(0)

    out["assessment_engagement"] = out["assessment_count"] * out["submission_rate"]

    # Risk-oriented feature
    out["low_engagement_flag"] = (
        (out["total_clicks"] <= out["total_clicks"].median()) &
        (out["assessment_count"] <= out["assessment_count"].median())
    ).astype(int)

    return out


def encode_categorical_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    Encode categorical columns using label encoding for compactness.
    One-hot encoding can be used later in clustering if needed.
    """
    out = df.copy()

    for col in columns:
        if col in out.columns:
            le = LabelEncoder()
            out[col] = out[col].astype(str)
            out[col] = le.fit_transform(out[col])

    return out


def select_final_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Keep only columns useful for clustering and analysis.
    """
    useful_columns = [
        "code_module",
        "code_presentation",
        "id_student",
        "gender",
        "region",
        "highest_education",
        "imd_band",
        "age_band",
        "disability",
        "final_result",
        "studied_credits",
        "num_of_prev_attempts",
        "date_registration",
        "total_clicks",
        "active_days",
        "avg_clicks_per_active_day",
        "max_clicks_per_day",
        "assessment_count",
        "avg_assessment_score",
        "std_assessment_score",
        "late_submissions",
        "on_time_submissions",
        "submission_rate",
        "activity_span",
        "clicks_per_course_day",
        "assessment_engagement",
        "low_engagement_flag",
    ]

    available = [c for c in useful_columns if c in df.columns]
    return df[available].copy()


if __name__ == "__main__":
    df = pd.read_csv(CLEANED_FILE)

    df = create_engagement_features(df)
    df = select_final_features(df)

    categorical_cols = [
        "gender",
        "region",
        "highest_education",
        "imd_band",
        "age_band",
        "disability",
        "final_result",
    ]

    df = encode_categorical_columns(df, categorical_cols)

    # Final fill for safety
    df = df.fillna(0)

    df.to_csv(ENGINEERED_FILE, index=False)
    print(f"Saved engineered dataset to: {ENGINEERED_FILE}")