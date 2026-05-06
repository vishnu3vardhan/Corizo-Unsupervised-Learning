# Abstract

This project explores student behavioral patterns using unsupervised learning techniques on the Open University Learning Analytics Dataset (OULAD). The objective is to identify hidden structures in student engagement and performance data without relying on predefined labels.

A comprehensive data pipeline was developed to integrate multiple relational datasets, including student demographics, virtual learning environment (VLE) interactions, and assessment records. Feature engineering was performed to capture meaningful behavioral indicators such as total engagement (clicks), activity frequency, assessment participation, and submission patterns.

Clustering techniques, particularly K-Means, were applied to the processed dataset after normalization. The optimal number of clusters was determined using silhouette analysis, which revealed two distinct and well-separated student groups.

The results indicate a strong correlation between student engagement and academic performance. One cluster represents highly engaged students who actively participate in course activities and achieve higher assessment scores, while the other cluster represents low-engagement students with minimal interaction and significantly lower performance.

This study demonstrates the effectiveness of unsupervised learning in uncovering actionable insights from educational data. The findings can support early identification of at-risk students and enable targeted interventions to improve learning outcomes.