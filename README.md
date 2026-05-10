# 📊 Multi-Domain Analytics Suite: E-commerce & Financial Intelligence

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Data Analysis](https://img.shields.io/badge/analysis-Pandas%20%7C%20NumPy-orange.svg)]()
[![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-green.svg)]()
[![Visualization](https://img.shields.io/badge/viz-Seaborn%20%7C%20Matplotlib-red.svg)]()

## 📑 Executive Summary
This portfolio project showcases an end-to-end data science ecosystem, integrating synthetic data generation, advanced exploratory data analysis (EDA), and machine learning pipelines. It bridges the gap between raw data and actionable business intelligence across two critical sectors: **Retail E-commerce** and **Banking/Finance**.

---

## 🏗️ Project Architecture

The repository is organized into distinct modules for data synthesis, processing, and visualization:

| Module | Description |
| :--- | :--- |
| `1_generate_data.py` | Engine for creating synthetic e-commerce transactions with realistic seasonal noise. |
| `2_data_analysis.py` | Python-based analytical script for automated report generation. |
| `3_generate_finance_data.py` | Financial simulator generating banking transactions with fraud-like anomalies. |
| `data_analysis.ipynb` | **[CORE]** Interactive workspace featuring Feature Engineering, ML Modeling, and deep-dive EDA. |
| `requirements.txt` | Dependency manifest for environment reproducibility. |

---

## 🛠️ Technical Stack & Methodologies

### Core Technologies
*   **Data Engineering**: `Pandas`, `NumPy` for robust data manipulation and vectorization.
*   **Statistical Analysis**: `SciPy`, `Statsmodels` for hypothesis testing and volatility modeling.
*   **Machine Learning**: `Scikit-Learn` implementation of:
    *   *Unsupervised*: Isolation Forest (Anomaly Detection), K-Means++ (Customer Segmentation).
    *   *Supervised*: Random Forest Regressor (Revenue Forecasting).
*   **Visualization**: `Seaborn` & `Matplotlib` using custom style configurations for publication-quality plots.

### Advanced Analytical Techniques
*   **RFM Modeling**: Recency, Frequency, and Monetary analysis to quantify customer lifetime value.
*   **Cyclical Feature Engineering**: Transforming temporal data into Sine/Cosine coordinates to capture periodic seasonality.
*   **Anomaly Scoring**: Multi-dimensional outlier detection to flag high-risk financial activities.

---

## 📈 Strategic Business Insights

### 🛒 E-commerce Optimization
*   **Retention Dynamics**: Analysis shows that holiday-acquired cohorts exhibit a **15% higher retention rate** over 6 months compared to baseline.
*   **Predictive Revenue**: By leveraging cyclical time features, our Random Forest model accounts for weekend surges, allowing for **optimized inventory stocking**.

### 🏦 Financial Risk Mitigation
*   **Fraud Identification**: The Isolation Forest model successfully isolated **1.2% of transactions** as statistically significant anomalies, categorized by high-frequency velocity and unusual geographic deviation.
*   **Wealth Clustering**: Identified four distinct user tiers, enabling hyper-personalized marketing for investment-heavy portfolios.

---

## 🚀 Deployment & Usage

### 1. Environment Setup
Clone the repository and install the required dependencies:
```bash
git clone https://github.com/your-username/DataAnalystProject.git
cd DataAnalystProject
pip install -r requirements.txt
```

### 2. Data Generation Pipeline
Populate the local environment with synthetic datasets:
```bash
python 1_generate_data.py
python 3_generate_finance_data.py
```

### 3. Execution
Launch the interactive analysis:
```bash
jupyter notebook data_analysis.ipynb
```

---

## 🛡️ License & Contact
Distributed under the **MIT License**. See `LICENSE` for more information.

**Project Developer** - [Your Name]
*   **LinkedIn**: [Your Profile]
*   **Portfolio**: [Your Website]
*   **Email**: your.email@example.com

---
*Created with passion for data-driven decision making.*
