import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

from config import PROCESSED_DIR

FIGURES_DIR = Path("figures")
FIGURES_DIR.mkdir(exist_ok=True)

df = pd.read_csv(PROCESSED_DIR / "clustered_data.csv")

plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x="cluster", y="avg_assessment_score")

plt.title("Assessment Score Distribution by Cluster")
plt.xlabel("Cluster")
plt.ylabel("Score")

plt.tight_layout()
plt.savefig(FIGURES_DIR / "score_distribution.png")
plt.show()

print("Saved score_distribution.png")