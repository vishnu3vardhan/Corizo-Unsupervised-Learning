import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from config import PROCESSED_DIR

# Load PCA data
df = pd.read_csv(PROCESSED_DIR / "pca_data.csv")

# Set style
sns.set(style="whitegrid")

# Create plot
plt.figure(figsize=(10, 7))

sns.scatterplot(
    data=df.sample(5000, random_state=42),
    x="PC1",
    y="PC2",
    hue="cluster",
    palette="Set1",
    alpha=0.6
)

plt.title("Student Behavior Clusters using PCA", fontsize=14, fontweight='bold')
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title="Cluster")

# Save figure
plt.savefig(PROCESSED_DIR / "pca_cluster_plot.png")

# Show plot
plt.show()