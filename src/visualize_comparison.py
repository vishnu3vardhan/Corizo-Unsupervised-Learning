import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

from config import PROCESSED_DIR

# Create figures folder if not exists
FIGURES_DIR = Path("figures")
FIGURES_DIR.mkdir(exist_ok=True)

# Load clustered data
df = pd.read_csv(PROCESSED_DIR / "clustered_data.csv")

# Select important features for comparison
features = [
    "total_clicks",
    "active_days",
    "avg_assessment_score",
    "assessment_count",
    "submission_rate"
]

# Compute mean values per cluster
cluster_means = df.groupby("cluster")[features].mean().reset_index()

# Melt data for seaborn
melted = cluster_means.melt(id_vars="cluster", var_name="feature", value_name="value")

# Plot
plt.figure(figsize=(12, 7))
sns.barplot(data=melted, x="feature", y="value", hue="cluster")

plt.title("Cluster Comparison of Student Behavior", fontsize=14, fontweight='bold')
plt.xticks(rotation=30)
plt.ylabel("Average Value")
plt.xlabel("Features")
plt.legend(title="Cluster")

plt.tight_layout()

# Save figure
plt.savefig(FIGURES_DIR / "cluster_comparison.png")

# Show plot
plt.show()

print("Saved cluster_comparison.png in figures/")