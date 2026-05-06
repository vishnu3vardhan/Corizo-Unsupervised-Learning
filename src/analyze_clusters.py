import pandas as pd
from config import PROCESSED_DIR

# Display all columns in output
pd.set_option('display.max_columns', None)

# Load clustered data
df = pd.read_csv(PROCESSED_DIR / "clustered_data.csv")

# Show cluster counts
print("\nCluster counts:")
print(df["cluster"].value_counts())

# Show average values per cluster
print("\nCluster-wise averages:")
cluster_summary = df.groupby("cluster").mean(numeric_only=True)

print(cluster_summary)

# Save it also (useful for report)
cluster_summary.to_csv(PROCESSED_DIR / "cluster_summary.csv")

print("\nSaved cluster summary!")