import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

from config import ENGINEERED_FILE, PROCESSED_DIR


def load_data():
    df = pd.read_csv(ENGINEERED_FILE)
    return df


def select_features(df):
    """
    Remove non-useful columns for clustering.
    """
    drop_cols = [
        "id_student",
        "code_module",
        "code_presentation",
        "final_result",  # avoid label leakage
    ]

    df = df.drop(columns=[col for col in drop_cols if col in df.columns])

    return df


def scale_data(df):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df)

    return scaled, scaler


def find_optimal_k(data):
    """
    Use Elbow + Silhouette method
    """
    results = []

    for k in range(2, 10):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(data)

        score = silhouette_score(data, labels)

        results.append((k, score))
        print(f"K={k}, Silhouette Score={score:.4f}")

    return results


def run_kmeans(data, k=4):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(data)

    return kmeans, labels


def apply_pca(data):
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(data)

    return reduced


def save_outputs(df_original, labels, reduced):
    output_df = df_original.copy()
    output_df["cluster"] = labels

    output_df.to_csv(PROCESSED_DIR / "clustered_data.csv", index=False)

    pca_df = pd.DataFrame(reduced, columns=["PC1", "PC2"])
    pca_df["cluster"] = labels
    pca_df.to_csv(PROCESSED_DIR / "pca_data.csv", index=False)

    print("Saved clustering outputs!")


def main():
    print("Loading data...")
    df = load_data()

    print("Selecting features...")
    df_features = select_features(df)

    print("Scaling data...")
    scaled_data, scaler = scale_data(df_features)

    print("Finding optimal K...")
    find_optimal_k(scaled_data)

    print("Running final KMeans...")
    model, labels = run_kmeans(scaled_data, k=2)

    print("Applying PCA...")
    reduced = apply_pca(scaled_data)

    print("Saving outputs...")
    save_outputs(df, labels, reduced)


if __name__ == "__main__":
    main()