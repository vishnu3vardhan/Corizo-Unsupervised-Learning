# Student Behavior Clustering using Unsupervised Learning

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Machine%20Learning-Unsupervised-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Dataset-OULAD-orange?style=for-the-badge"/>
</p>

---

##  Project Snapshot

> *Goal:* Discover hidden student behavior patterns without labels
>  *Method:* K-Means Clustering + Feature Engineering
>  *Outcome:* Identified At-Risk vs High-Performing students

---

##  Table of Contents

* [Overview](#-overview)
* [Problem Statement](#-problem-statement)
* [Solution Approach](#-solution-approach)
* [Project Structure](#-project-structure)
* [How to Run](#-how-to-run)
* [Results](#-results)
* [Visual Insights](#-visual-insights)
* [Key Insights](#-key-insights)
* [Applications](#-applications)
* [Tech Stack](#-tech-stack)
* [Future Work](#-future-work)

---

##  Overview

This project uses *unsupervised learning* to analyze student behavior from the Open University dataset.

Instead of relying on labels like pass/fail, the model learns patterns from:

* Student engagement
* Learning activity
* Assessment participation

---

## Problem Statement

Educational systems often fail to detect struggling students early.

 This project answers:

> *Can we identify at-risk students purely from behavior patterns?*

---

## Solution Approach

<details>
<summary>Click to expand full pipeline</summary>

### Data Processing

* Merged multiple relational datasets
* Cleaned missing values
* Created unified student-level dataset

### Feature Engineering

* Total engagement (clicks)
* Active days
* Assessment participation
* Submission behavior

### Modeling

* Standardized features
* Applied *K-Means Clustering*
* Used *Silhouette Score* for optimal K

###  Visualization

* PCA for dimensionality reduction
* Cluster comparison charts
* Behavioral insights

</details>

---

## Project Structure

bash
data/
src/
figures/
reports/
README.md


---

## How to Run

bash
# Clone repo
git clone https://github.com/your-username/oulad-student-clustering.git

# Setup environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run pipeline
python src/data_pipeline.py
python src/clustering.py
python src/analyze_clusters.py


---

## Results

### Optimal Clusters: *2*

| Cluster | Type            | Behavior                       |
| ------- | --------------- | ------------------------------ |
| 🔵 0    | High Performers | High engagement, strong scores |
| 🔴 1    | At-Risk         | Low activity, poor performance |

---

## Visual Insights

### PCA Cluster Distribution

<p align="center">
  <img src="figures/pca_cluster_plot.png" width="600"/>
</p>

---

### Feature Comparison

<p align="center">
  <img src="figures/cluster_comparison.png" width="600"/>
</p>

---

### Cluster Size

<p align="center">
  <img src="figures/cluster_size.png" width="400"/>
</p>

---

### Score Distribution

<p align="center">
  <img src="figures/score_distribution.png" width="500"/>
</p>

---

### Correlation Heatmap

<p align="center">
  <img src="figures/correlation_heatmap.png" width="600"/>
</p>

---

## Key Insights

* Engagement is the strongest predictor of success
*  Low activity students are clearly identifiable
*  Model separated students without labels
*  Strong gap between high and low performers

---

## Applications

* Early warning systems
* Personalized learning paths
* Academic intervention strategies
* Institutional decision-making

---

## Tech Stack

| Category      | Tools               |
| ------------- | ------------------- |
| Language      | Python              |
| Data          | Pandas, NumPy       |
| ML            | Scikit-learn        |
| Visualization | Matplotlib, Seaborn |

---

##  Future Work

* 🔹 DBSCAN & Hierarchical clustering
* 🔹 Predictive modeling (supervised learning)
* 🔹 Streamlit dashboard
* 🔹 Real-time analytics system

---

## Authors

*Vishnu Vardhan* and
*Amrithaa*
---

---

##  License

MIT License
