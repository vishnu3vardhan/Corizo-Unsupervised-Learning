import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

from config import PROCESSED_DIR

FIGURES_DIR = Path("figures")
FIGURES_DIR.mkdir(exist_ok=True)

df = pd.read_csv(PROCESSED_DIR / "clustered_data.csv")

# Select numeric columns only
numeric_df = df.select_dtypes(include="number")

plt.figure(figsize=(10, 8))
sns.heatmap(numeric_df.corr(), cmap="coolwarm", annot=False)

plt.title("Feature Correlation Heatmap")
plt.tight_layout()

plt.savefig(FIGURES_DIR / "correlation_heatmap.png")
plt.show()

print("Saved correlation_heatmap.png")