from pathlib import Path

# Base paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"

# Create directories if they do not exist
for directory in [RAW_DIR, INTERIM_DIR, PROCESSED_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Raw OULAD files
RAW_FILES = {
    "courses": RAW_DIR / "courses.csv",
    "assessments": RAW_DIR / "assessments.csv",
    "vle": RAW_DIR / "vle.csv",
    "studentInfo": RAW_DIR / "studentInfo.csv",
    "studentRegistration": RAW_DIR / "studentRegistration.csv",
    "studentAssessment": RAW_DIR / "studentAssessment.csv",
    "studentVle": RAW_DIR / "studentVle.csv",
}

# Output files
MERGED_FILE = INTERIM_DIR / "merged_students.csv"
CLEANED_FILE = INTERIM_DIR / "cleaned_students.csv"
ENGINEERED_FILE = INTERIM_DIR / "engineered_features.csv"

# Useful columns for clustering later
NUMERIC_FEATURES = [
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
    "date_registration",
    "studied_credits",
    "num_of_prev_attempts",
]

CATEGORICAL_FEATURES = [
    "gender",
    "region",
    "highest_education",
    "imd_band",
    "age_band",
    "disability",
    "final_result",
]