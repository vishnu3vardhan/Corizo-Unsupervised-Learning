import pandas as pd
import numpy as np

from config import MERGED_FILE, CLEANED_FILE
from load_data import load_oulad_data


def aggregate_student_vle(student_vle: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate VLE clickstream data to student-course level.
    """
    agg = student_vle.groupby(["code_module", "code_presentation", "id_student"]).agg(
        total_clicks=("sum_click", "sum"),
        active_days=("date", "nunique"),
        max_clicks_per_day=("sum_click", "max"),
        avg_clicks_per_day=("sum_click", "mean"),
        std_clicks_per_day=("sum_click", "std"),
        first_activity_day=("date", "min"),
        last_activity_day=("date", "max"),
    ).reset_index()

    agg["std_clicks_per_day"] = agg["std_clicks_per_day"].fillna(0)
    agg["avg_clicks_per_active_day"] = agg["total_clicks"] / agg["active_days"].replace(0, np.nan)
    agg["avg_clicks_per_active_day"] = agg["avg_clicks_per_active_day"].fillna(0)

    return agg


def aggregate_student_assessment(student_assessment: pd.DataFrame, assessments: pd.DataFrame) -> pd.DataFrame:
    """
    Build student-level assessment features by joining assessment metadata first.
    """
    merged = student_assessment.merge(
        assessments,
        on="id_assessment",
        how="left"
    )

    # late_days = submission_date - due_date
    merged["late_days"] = merged["date_submitted"].astype(float) - merged["date"].astype(float)
    agg = merged.groupby(["code_module", "code_presentation", "id_student"]).agg(
        assessment_count=("id_assessment", "count"),
        avg_assessment_score=("score", "mean"),
        std_assessment_score=("score", "std"),
        late_submissions=("late_days", lambda x: (x > 0).sum()), 
        on_time_submissions=("late_days", lambda x: (x <= 0).sum()),
        avg_late_days=("late_days", "mean"),
    ).reset_index()

    agg["std_assessment_score"] = agg["std_assessment_score"].fillna(0)
    agg["avg_late_days"] = agg["avg_late_days"].fillna(0)
    agg["avg_assessment_score"] = agg["avg_assessment_score"].fillna(0)

    total_submissions = agg["late_submissions"] + agg["on_time_submissions"]
    agg["submission_rate"] = total_submissions.replace(0, np.nan)
    agg["submission_rate"] = agg["assessment_count"] / agg["submission_rate"]
    agg["submission_rate"] = agg["submission_rate"].replace([np.inf, -np.inf], np.nan).fillna(0)

    return agg


def merge_all_tables() -> pd.DataFrame:
    """
    Merge all relevant OULAD tables into one master dataset.
    """
    data = load_oulad_data()

    student_info = data["studentInfo"]
    student_registration = data["studentRegistration"]
    student_vle = data["studentVle"]
    student_assessment = data["studentAssessment"]
    assessments = data["assessments"]

    # Aggregate behavioral tables
    vle_agg = aggregate_student_vle(student_vle)
    assessment_agg = aggregate_student_assessment(student_assessment, assessments)

    # Merge base student data
    df = student_info.merge(
        student_registration,
        on=["code_module", "code_presentation", "id_student"],
        how="left"
    )

    df = df.merge(
        vle_agg,
        on=["code_module", "code_presentation", "id_student"],
        how="left"
    )

    df = df.merge(
        assessment_agg,
        on=["code_module", "code_presentation", "id_student"],
        how="left"
    )

    # Fill missing numerical values
    numeric_cols = df.select_dtypes(include=["number"]).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)

    # Fill missing categorical values
    cat_cols = df.select_dtypes(include=["object"]).columns
    for col in cat_cols:
        df[col] = df[col].fillna("Unknown")

    return df


def clean_merged_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleaning: remove duplicates and standardize column names.
    """
    df = df.drop_duplicates()

    # Standardize column names
    df.columns = [c.strip().lower() for c in df.columns]

    # Remove obviously useless or empty columns if any appear
    for col in df.columns:
        if df[col].nunique(dropna=False) <= 1:
            pass

    return df


if __name__ == "__main__":
    merged = merge_all_tables()
    merged.to_csv(MERGED_FILE, index=False)
    print(f"Saved merged file to: {MERGED_FILE}")

    cleaned = clean_merged_data(merged)
    cleaned.to_csv(CLEANED_FILE, index=False)
    print(f"Saved cleaned file to: {CLEANED_FILE}")