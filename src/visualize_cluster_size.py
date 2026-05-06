import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

from config import PROCESSED_DIR

FIGURES_DIR = Path("figures")
FIGURES_DIR.mkdir(exist_ok=True)

df = pd.read_csv(PROCESSED_DIR / "clustered_data.csv")

plt.figure(figsize=(6, 5))
sns.countplot(data=df, x="cluster")

plt.title("Cluster Size Distribution")
plt.xlabel("Cluster")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.savefig(FIGURES_DIR / "cluster_size.png")
plt.show()

print("Saved cluster_size.png")