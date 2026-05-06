from preprocess import merge_all_tables, clean_merged_data
from feature_engineering import (
    create_engagement_features,
    select_final_features,
    encode_categorical_columns,
)
from config import MERGED_FILE, CLEANED_FILE, ENGINEERED_FILE


def main():
    print("Loading and merging raw tables...")
    merged = merge_all_tables()
    merged.to_csv(MERGED_FILE, index=False)

    print("Cleaning merged data...")
    cleaned = clean_merged_data(merged)
    cleaned.to_csv(CLEANED_FILE, index=False)

    print("Creating engineered features...")
    engineered = create_engagement_features(cleaned)
    engineered = select_final_features(engineered)

    categorical_cols = [
        "gender",
        "region",
        "highest_education",
        "imd_band",
        "age_band",
        "disability",
        "final_result",
    ]
    engineered = encode_categorical_columns(engineered, categorical_cols)
    engineered = engineered.fillna(0)

    engineered.to_csv(ENGINEERED_FILE, index=False)
    print(f"First half completed. Final file saved at: {ENGINEERED_FILE}")


if __name__ == "__main__":
    main()