import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run_analysis():
    # Set gaya visualisasi
    sns.set_theme(style="whitegrid")
    plt.rcParams.update({'figure.max_open_warning': 0})
    
    file_path = "telecom_churn_data.csv"
    if not os.path.exists(file_path):
        print(f"Error: {file_path} tidak ditemukan. Jalankan 01_data_generation.py terlebih dahulu.")
        return

    print("=== Memuat Data ===")
    df = pd.read_csv(file_path)
    print(f"Total baris: {df.shape[0]}, Total kolom: {df.shape[1]}\n")

    print("=== Data Cleaning & Preprocessing ===")
    # Cek Missing Values
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print("Ditemukan missing values:")
        print(missing[missing > 0])
        # Imputasi total charges dengan nilai median dari data yang ada
        median_total_charge = df['TotalCharges'].median()
        df['TotalCharges'].fillna(median_total_charge, inplace=True)
        print("Missing values pada 'TotalCharges' telah diisi dengan nilai median.\n")
    else:
        print("Tidak ditemukan missing values.\n")

    # Pastikan tipe data sesuai
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'])

    print("=== Exploratory Data Analysis (EDA) ===")
    
    # 1. Distribusi Churn
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='Churn', palette='Set2')
    plt.title('Distribusi Churn Pelanggan')
    plt.ylabel('Jumlah Pelanggan')
    plt.savefig('plot_1_churn_distribution.png')
    plt.close()
    print("Grafik 'plot_1_churn_distribution.png' berhasil disimpan.")

    # 2. Churn berdasarkan Contract Type
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='Contract', hue='Churn', palette='Set2')
    plt.title('Churn Pelanggan Berdasarkan Tipe Kontrak')
    plt.ylabel('Jumlah Pelanggan')
    plt.savefig('plot_2_churn_by_contract.png')
    plt.close()
    print("Grafik 'plot_2_churn_by_contract.png' berhasil disimpan.")

    # 3. Distribusi Tenure (Lama Berlangganan) terhadap Churn
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x='Tenure', hue='Churn', multiple='stack', bins=30, palette='Set2')
    plt.title('Distribusi Tenure Berdasarkan Churn')
    plt.xlabel('Tenure (Bulan)')
    plt.ylabel('Jumlah Pelanggan')
    plt.savefig('plot_3_tenure_vs_churn.png')
    plt.close()
    print("Grafik 'plot_3_tenure_vs_churn.png' berhasil disimpan.")

    # 4. Monthly Charges terhadap Churn
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x='Churn', y='MonthlyCharges', palette='Set2')
    plt.title('Distribusi Biaya Bulanan Berdasarkan Churn')
    plt.ylabel('Biaya Bulanan (USD)')
    plt.savefig('plot_4_monthly_charges_vs_churn.png')
    plt.close()
    print("Grafik 'plot_4_monthly_charges_vs_churn.png' berhasil disimpan.")

    print("\n=== Business Insights ===")
    churn_rate = (df['Churn'] == 'Yes').mean() * 100
    print(f"1. Overall Churn Rate: {churn_rate:.2f}%")
    print("2. Pelanggan dengan kontrak 'Month-to-month' memiliki tingkat churn yang paling tinggi. Disarankan untuk memberikan insentif agar pelanggan beralih ke kontrak tahunan.")
    print("3. Pelanggan baru (Tenure rendah) sangat rentan untuk churn di 6 bulan pertama. Diperlukan program onboarding yang lebih baik.")
    print("4. Pelanggan yang melakukan churn rata-rata memiliki tagihan bulanan (Monthly Charges) yang lebih tinggi. Evaluasi kembali struktur harga atau berikan paket diskon untuk menekan churn.")

if __name__ == "__main__":
    run_analysis()
