# Findings and Insights

## Overview

The clustering analysis on the OULAD dataset revealed two distinct student groups based on behavioral and performance-related features. These clusters highlight clear differences in engagement levels, assessment participation, and academic outcomes.

---

## Cluster Visualization (PCA)

![PCA Clusters](../figures/pca_cluster_plot.png)

### Explanation:
The PCA (Principal Component Analysis) plot reduces high-dimensional student behavior data into two dimensions for visualization. Each point represents a student, and colors indicate cluster membership.

The clear separation between clusters indicates that the model successfully identified distinct behavioral groups. One cluster is densely packed and represents highly engaged students, while the other reflects low-engagement students.

---

## Cluster Comparison (Key Features)

![Cluster Comparison](../figures/cluster_comparison.png)

### Explanation:
This bar chart compares key behavioral features across clusters.

Key observations:
- Cluster 0 shows significantly higher engagement (clicks, activity days)
- Assessment participation is much higher in Cluster 0
- Submission rates are near complete for Cluster 0
- Cluster 1 consistently shows low values across all engagement metrics

This visualization clearly highlights the behavioral gap between the two groups.

---

## Cluster Size Distribution

![Cluster Size](../figures/cluster_size.png)

### Explanation:
This plot shows the number of students in each cluster.

- Cluster 0: Majority of students (high engagement group)
- Cluster 1: Smaller but significant portion (at-risk group)

This indicates that while most students are active, a considerable number are disengaged and require attention.

---

## Assessment Score Distribution

![Score Distribution](../figures/score_distribution.png)

### Explanation:
The boxplot shows the distribution of assessment scores for each cluster.

- Cluster 0: Higher median and tighter distribution → consistent performance
- Cluster 1: Very low scores with little variation → consistently poor performance

This confirms that engagement directly impacts academic success.

---

## Feature Correlation Heatmap

![Correlation Heatmap](../figures/correlation_heatmap.png)

### Explanation:
The heatmap shows relationships between numerical features.

Key insights:
- Strong positive correlation between engagement metrics (clicks, active days)
- Positive relationship between engagement and assessment scores
- Low engagement features correlate with poor performance

This reinforces the idea that student activity is a strong predictor of success.

---

## Cluster 0: Consistent High Achievers

### Key Characteristics:
- High total engagement (~1869 clicks)
- Regular activity (~83 active days)
- High assessment participation (~8 assessments)
- Strong performance (~76 average score)
- High submission rate (~1.02)

### Interpretation:
These students are highly engaged, consistent, and perform well academically.

### Persona:
**Consistent High Achievers**

---

## Cluster 1: Low Engagement / At-Risk Learners

### Key Characteristics:
- Low engagement (~148 clicks)
- Minimal activity (~9 active days)
- Very low assessment participation (~1 assessment)
- Poor performance (~28 average score)
- Low submission rate (~0.45)

### Interpretation:
These students are disengaged and show clear signs of academic risk.

### Persona:
**At-Risk or Disengaged Learners**

---

## Key Insight

The clustering results reveal a strong relationship between student engagement and academic performance.

Even without using performance labels during training, the model naturally separated students into:
- High-performing, engaged learners
- Low-performing, disengaged learners

This demonstrates the effectiveness of unsupervised learning in uncovering meaningful patterns.

---

## Practical Implications

- Early identification of at-risk students
- Targeted interventions for disengaged learners
- Improved academic support strategies
- Data-driven decision-making in education

---

## Conclusion

The project successfully applied unsupervised learning to identify meaningful student behavior patterns. The findings emphasize the critical role of engagement in academic success and highlight the potential of machine learning in educational analytics.