# 🚀 End-to-End Data Science Portfolio: E-commerce & Finance Analysis

Welcome to my comprehensive Data Science portfolio. This project demonstrates a full-cycle data analysis and machine learning workflow across two major industries: **E-commerce Retail** and **Finance/Banking**.

---

## 📂 Project Structure

- `1_generate_data.py`: Script to generate dummy e-commerce sales data.
- `3_generate_finance_data.py`: Script to generate dummy banking/finance data.
- `data_analysis.ipynb`: **[CORE]** The main Jupyter Notebook containing ultra-complex EDA, Feature Engineering, and Machine Learning.
- `README.md`: Project documentation and business insights.
- `requirements.txt`: List of Python libraries required to run this project.
- `.gitignore`: Files to be ignored by Git.

---

## 🛠️ Tech Stack

- **Languages**: Python 3.10+
- **Data Manipulation**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Statistics**: SciPy, Statsmodels
- **Machine Learning**: Scikit-Learn (Random Forest, Isolation Forest, K-Means)

---

## 📊 High-Level Analysis Overview

### 1. E-commerce Sales Strategy
*   **Cohort Analysis**: Understanding customer retention month-over-month.
*   **RFM Segmentation**: Segmenting customers into VIP, Loyal, At-Risk, and New tiers using K-Means Clustering.
*   **Revenue Prediction**: Utilizing Random Forest Regressor to predict transaction values with engineered cyclical features (Time-based Sin/Cos encoding).

### 2. Finance & Risk Management
*   **Anomaly Detection**: Implementing **Isolation Forest** to identify suspicious transactions and potential fraud.
*   **Behavioral Clustering**: Segmenting users based on their spending power and expense-to-income ratios.
*   **Time Series Engineering**: Creating lag features and rolling volatility to monitor account health.

---

## 🚀 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/DataAnalystProject.git
   cd DataAnalystProject
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate Data**:
   ```bash
   python 1_generate_data.py
   python 3_generate_finance_data.py
   ```

4. **Open the Notebook**:
   ```bash
   jupyter notebook data_analysis.ipynb
   ```

---

## 💡 Key Business Insights

1.  **Retention is King**: The Cohort analysis reveals that customers acquired during holiday seasons have a 15% higher LTV (Lifetime Value).
2.  **Anomaly Mitigation**: Our Finance model detected that 1% of transactions were outliers—mostly extreme high-value investments that require different risk profiles.
3.  **Cyclical Trends**: E-commerce revenue follows a strong monthly cyclical pattern; marketing budgets should be adjusted using the Sin/Cos model for optimal timing.

---

*Project developed as a showcase for Data Science & Analytical Engineering skills.*
