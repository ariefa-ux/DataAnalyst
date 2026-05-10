import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style for seaborn
sns.set_theme(style="whitegrid", palette="muted")

def run_analysis():
    print("Mulai Analisis Data...")
    
    # ---------------------------------------------------------
    # STEP 1: Data Loading
    # ---------------------------------------------------------
    print("\n--- STEP 1: Data Loading ---")
    df = pd.DataFrame()
    try:
        df = pd.read_csv('sales_data.csv')
        print(f"Dataset berhasil dimuat dengan {df.shape[0]} baris dan {df.shape[1]} kolom.")
    except FileNotFoundError:
        print("Error: File 'sales_data.csv' tidak ditemukan. Jalankan 1_generate_data.py terlebih dahulu.")

        return

    # ---------------------------------------------------------
    # STEP 2: Data Cleaning & Preprocessing
    # ---------------------------------------------------------
    print("\n--- STEP 2: Data Cleaning & Preprocessing ---")
    
    # 2a. Mengatasi Missing Values
    missing_info = df.isnull().sum()
    print("Jumlah Missing Values sebelum dibersihkan:\n", missing_info[missing_info > 0])
    
    # Isi City yang kosong dengan 'Unknown'
    df['City'] = df['City'].fillna('Unknown')
    
    # Isi Discount yang kosong dengan 0.0 (asumsi tidak ada diskon)
    df['Discount'] = df['Discount'].fillna(0.0)
    
    # 2b. Menangani Invalid Data (Negative Quantity)
    # Asumsi: nilai negatif pada Quantity adalah typo atau barang retur.
    # Untuk analisis penjualan ini, kita hanya ambil Quantity > 0.
    invalid_qty_count = df[df['Quantity'] <= 0].shape[0]
    print(f"\nMenghapus {invalid_qty_count} baris dengan Quantity <= 0 (kemungkinan retur/typo).")
    df = df[df['Quantity'] > 0].copy()
    
    # 2c. Feature Engineering (Membuat kolom baru yang berguna)
    # Ubah 'Date' ke format datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Ekstrak Tahun-Bulan untuk analisis tren
    df['YearMonth'] = df['Date'].dt.to_period('M').astype(str)
    
    # Hitung Total Sales: (Harga * Jumlah) - Diskon
    # Jika diskon dalam persentase (0 - 1.0)
    df['Total_Sales'] = df['Price'] * df['Quantity'] * (1 - df['Discount'])
    
    print("\nData Cleaning Selesai. Info dataset saat ini:")
    print(df.info())

    # ---------------------------------------------------------
    # STEP 3: Exploratory Data Analysis (EDA) & Visualization
    # ---------------------------------------------------------
    print("\n--- STEP 3: Exploratory Data Analysis & Visualization ---")
    
    # Pastikan folder visualisasi ada (opsional, di sini kita simpan di current directory)
    
    # 3a. Monthly Sales Trend (Tren Penjualan Bulanan)
    print("Membuat grafik Tren Penjualan Bulanan...")
    monthly_sales = df.groupby('YearMonth')['Total_Sales'].sum().reset_index()
    monthly_sales = monthly_sales.sort_values('YearMonth')
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=monthly_sales, x='YearMonth', y='Total_Sales', marker='o', color='b')
    plt.title('Tren Penjualan Bulanan (2023-2024)', fontsize=16)
    plt.xlabel('Bulan', fontsize=12)
    plt.ylabel('Total Penjualan (Rp)', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('plot_1_monthly_sales_trend.png', dpi=300)
    plt.close()
    
    # 3b. Sales by Category (Penjualan berdasarkan Kategori)
    print("Membuat grafik Penjualan berdasarkan Kategori...")
    category_sales = df.groupby('Product_Category')['Total_Sales'].sum().reset_index()
    category_sales = category_sales.sort_values('Total_Sales', ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=category_sales, x='Product_Category', y='Total_Sales', palette='viridis')
    plt.title('Total Penjualan Berdasarkan Kategori', fontsize=16)
    plt.xlabel('Kategori Produk', fontsize=12)
    plt.ylabel('Total Penjualan (Rp)', fontsize=12)
    plt.tight_layout()
    plt.savefig('plot_2_sales_by_category.png', dpi=300)
    plt.close()

    # 3c. Top 5 Products by Sales (5 Produk Terlaris)
    print("Membuat grafik 5 Produk Terlaris...")
    top_products = df.groupby('Product_Name')['Total_Sales'].sum().reset_index()
    top_products = top_products.sort_values('Total_Sales', ascending=False).head(5)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_products, y='Product_Name', x='Total_Sales', palette='magma')
    plt.title('Top 5 Produk dengan Penjualan Tertinggi', fontsize=16)
    plt.xlabel('Total Penjualan (Rp)', fontsize=12)
    plt.ylabel('Nama Produk', fontsize=12)
    plt.tight_layout()
    plt.savefig('plot_3_top_products.png', dpi=300)
    plt.close()

    # 3d. Sales Distribution by City (Distribusi Penjualan per Kota)
    print("Membuat grafik Distribusi Penjualan per Kota...")
    city_sales = df.groupby('City')['Total_Sales'].sum().reset_index()
    city_sales = city_sales.sort_values('Total_Sales', ascending=False)
    
    plt.figure(figsize=(10, 6))
    plt.pie(city_sales['Total_Sales'], labels=city_sales['City'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
    plt.title('Distribusi Penjualan Berdasarkan Kota', fontsize=16)
    plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.tight_layout()
    plt.savefig('plot_4_sales_by_city.png', dpi=300)
    plt.close()
    
    # ---------------------------------------------------------
    # STEP 4: Business Insights Summary
    # ---------------------------------------------------------
    print("\n--- STEP 4: Analisis Selesai ---")
    print("Semua grafik berhasil disimpan (plot_1_*.png s/d plot_4_*.png).")
    
    # Tampilkan top insight singkat
    best_month = monthly_sales.iloc[monthly_sales['Total_Sales'].argmax()]['YearMonth']
    best_category = category_sales.iloc[0]['Product_Category']
    best_city = city_sales.iloc[0]['City']
    
    print("\n[Ringkasan Insight Singkat]:")
    print(f"- Bulan dengan penjualan tertinggi: {best_month}")
    print(f"- Kategori produk paling menguntungkan: {best_category}")
    print(f"- Kota dengan kontribusi penjualan terbesar: {best_city}")
    
if __name__ == "__main__":
    run_analysis()
