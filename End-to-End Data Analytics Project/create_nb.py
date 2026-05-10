import nbformat as nbf

nb = nbf.v4.new_notebook()

# Markdown 1
md1 = """# End-to-End Data Analytics Project: Telecom Customer Churn

Proyek ini mendemonstrasikan proses end-to-end data analytics mulai dari:
1. **Pembuatan Data (Data Generation)**
2. **Pembersihan & Pra-pemrosesan Data (Data Cleaning & Preprocessing)**
3. **Analisis Data Eksploratif (Exploratory Data Analysis / EDA)**
4. **Penyimpulan Wawasan Bisnis (Business Insights & Recommendations)**

**Konteks Bisnis:**
Sebuah perusahaan telekomunikasi ingin memahami mengapa pelanggannya berhenti berlangganan (Churn). Dengan menganalisis data pelanggan, layanan yang digunakan, dan tagihan, kita dapat menemukan faktor-faktor utama yang memengaruhi churn dan memberikan rekomendasi strategis."""

# Code 1
c1 = """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import warnings

warnings.filterwarnings('ignore')
sns.set_theme(style="whitegrid")"""

# Markdown 2
md2 = """## 1. Pembuatan Data (Data Generation)
Karena ini adalah proyek simulasi, kita akan men-generate dataset sintetik yang realistis."""

# Code 2
c2 = """def generate_telecom_data(num_records=5000):
    np.random.seed(42)
    random.seed(42)

    customer_ids = [f"CUST-{str(i).zfill(5)}" for i in range(1, num_records + 1)]
    genders = np.random.choice(['Male', 'Female'], size=num_records)
    ages = np.random.randint(18, 75, size=num_records)
    tenures = np.random.randint(0, 73, size=num_records)
    contract_types = np.random.choice(['Month-to-month', 'One year', 'Two year'], size=num_records, p=[0.5, 0.3, 0.2])
    internet_services = np.random.choice(['DSL', 'Fiber optic', 'No'], size=num_records, p=[0.35, 0.45, 0.20])
    
    monthly_charges = []
    total_charges = []
    churn = []

    for i in range(num_records):
        base = 20
        if internet_services[i] == 'DSL': base += 30
        elif internet_services[i] == 'Fiber optic': base += 50
        monthly = base + random.uniform(-5, 15)
        monthly_charges.append(round(monthly, 2))
        
        total = 0.0 if tenures[i] == 0 else monthly * tenures[i] + random.uniform(-20, 20)
        
        # Simulasi missing values
        if random.random() < 0.01:
            total_charges.append(np.nan)
        else:
            total_charges.append(max(0, round(total, 2)))

        churn_prob = 0.1
        if contract_types[i] == 'Month-to-month': churn_prob += 0.3
        elif contract_types[i] == 'Two year': churn_prob -= 0.08
        if internet_services[i] == 'Fiber optic': churn_prob += 0.15
        if tenures[i] < 6: churn_prob += 0.2
        elif tenures[i] > 24: churn_prob -= 0.15
        if monthly > 70: churn_prob += 0.1
            
        churn_prob = max(0.01, min(0.99, churn_prob))
        churn.append('Yes' if random.random() < churn_prob else 'No')

    return pd.DataFrame({
        'CustomerID': customer_ids, 'Gender': genders, 'Age': ages,
        'Tenure': tenures, 'InternetService': internet_services,
        'Contract': contract_types, 'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges, 'Churn': churn
    })

df_raw = generate_telecom_data(5000)
df_raw.to_csv("telecom_churn_data.csv", index=False)
df_raw.head()"""

# Markdown 3
md3 = """## 2. Pembersihan & Pra-pemrosesan Data
Kita akan memuat data, mengecek nilai yang hilang (missing values), dan melakukan imputasi jika diperlukan."""

# Code 3
c3 = """df = pd.read_csv("telecom_churn_data.csv")
print("Informasi Dataset:")
df.info()

print("\\nMissing Values:")
print(df.isnull().sum())"""

# Code 4
c4 = """# Imputasi Missing Values pada TotalCharges dengan nilai median
median_total = df['TotalCharges'].median()
df['TotalCharges'].fillna(median_total, inplace=True)

# Verifikasi
print("Missing values setelah imputasi:", df['TotalCharges'].isnull().sum())"""

# Markdown 4
md4 = """## 3. Analisis Data Eksploratif (EDA)
Sekarang kita akan memvisualisasikan data untuk melihat pola dan korelasi terkait Churn."""

# Code 5
c5 = """# 1. Distribusi Target Variabel (Churn)
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Churn', palette='Set2')
plt.title('Distribusi Pelanggan Churn vs Retained')
plt.show()

churn_rate = (df['Churn'] == 'Yes').mean() * 100
print(f"Persentase Churn: {churn_rate:.2f}%")"""

# Code 6
c6 = """# 2. Churn berdasarkan Tipe Kontrak
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Contract', hue='Churn', palette='Set2')
plt.title('Churn Pelanggan Berdasarkan Tipe Kontrak')
plt.show()"""

# Code 7
c7 = """# 3. Churn berdasarkan Durasi Berlangganan (Tenure)
plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='Tenure', hue='Churn', multiple='stack', bins=36, palette='Set2', kde=True)
plt.title('Distribusi Tenure (Bulan) Terhadap Churn')
plt.show()"""

# Code 8
c8 = """# 4. Distribusi Biaya Bulanan terhadap Churn
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Churn', y='MonthlyCharges', palette='Set2')
plt.title('Distribusi Biaya Bulanan (Monthly Charges) Berdasarkan Churn')
plt.show()"""

# Markdown 5
md5 = """## 4. Kesimpulan & Rekomendasi Bisnis (Actionable Insights)

Berdasarkan analisis di atas, kita dapat merumuskan insight dan rekomendasi berikut:

1. **Risiko pada Kontrak Jangka Pendek:**
   - **Insight:** Mayoritas pelanggan yang churn adalah mereka yang memiliki kontrak *Month-to-month*.
   - **Rekomendasi:** Berikan insentif atau promosi khusus bagi pelanggan *Month-to-month* untuk beralih ke kontrak tahunan (*One year* atau *Two year*).

2. **Masa Kritis Pelanggan Baru:**
   - **Insight:** Tingkat churn sangat tinggi pada 6 bulan pertama (*low tenure*).
   - **Rekomendasi:** Tingkatkan *Customer Experience* selama fase *onboarding*. Tim Customer Success harus lebih proaktif memandu dan membantu pelanggan baru agar mendapatkan nilai maksimal dari layanan.

3. **Sensitivitas Harga:**
   - **Insight:** Pelanggan yang churn cenderung memiliki biaya bulanan (*Monthly Charges*) yang lebih tinggi.
   - **Rekomendasi:** Evaluasi kembali strategi *pricing*. Pertimbangkan untuk menawarkan paket bundling layanan (Internet + TV/Telepon) dengan harga diskon, atau sediakan opsi *downgrade* layanan sementara sebelum pelanggan memutuskan untuk berhenti sepenuhnya.
"""

nb.cells = [
    nbf.v4.new_markdown_cell(md1),
    nbf.v4.new_code_cell(c1),
    nbf.v4.new_markdown_cell(md2),
    nbf.v4.new_code_cell(c2),
    nbf.v4.new_markdown_cell(md3),
    nbf.v4.new_code_cell(c3),
    nbf.v4.new_code_cell(c4),
    nbf.v4.new_markdown_cell(md4),
    nbf.v4.new_code_cell(c5),
    nbf.v4.new_code_cell(c6),
    nbf.v4.new_code_cell(c7),
    nbf.v4.new_code_cell(c8),
    nbf.v4.new_markdown_cell(md5)
]

with open("end_to_end_analytics.ipynb", "w", encoding="utf-8") as f:
    nbf.write(nb, f)
print("Notebook end_to_end_analytics.ipynb berhasil dibuat!")
