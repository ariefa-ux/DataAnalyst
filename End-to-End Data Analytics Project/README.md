# End-to-End Data Analytics Project: Telecom Customer Churn

Proyek ini adalah contoh komprehensif dari alur kerja Data Analytics, berfokus pada studi kasus **Customer Churn** (Berhentinya pelanggan menggunakan layanan) pada perusahaan telekomunikasi fiktif.

## 📂 Struktur Proyek
- `01_data_generation.py`: Skrip untuk menghasilkan data sintetik simulasi pelanggan telekomunikasi (`telecom_churn_data.csv`).
- `02_data_analysis.py`: Skrip untuk membersihkan data (Data Cleaning), melakukan Exploratory Data Analysis (EDA), dan mengekspor visualisasi data menjadi file `.png`.
- `end_to_end_analytics.ipynb`: Versi interaktif (Jupyter Notebook) yang mencakup seluruh proses dari awal hingga akhir, dilengkapi dengan penjelasan naratif dan kesimpulan bisnis.

## 🚀 Cara Menjalankan Proyek

### 1. Prasyarat
Pastikan Anda telah menginstal pustaka Python yang dibutuhkan:
```bash
pip install pandas numpy matplotlib seaborn jupyter nbformat
```

### 2. Eksekusi Versi Skrip Python (.py)
Jalankan skrip secara berurutan di terminal Anda:

**Langkah 1: Hasilkan Data**
```bash
python 01_data_generation.py
```
Ini akan membuat file `telecom_churn_data.csv`.

**Langkah 2: Analisis Data**
```bash
python 02_data_analysis.py
```
Ini akan memuat data, membersihkan *missing values*, mencetak wawasan ke terminal, dan menghasilkan file grafik (seperti `plot_1_churn_distribution.png`).

### 3. Eksekusi Versi Jupyter Notebook (.ipynb)
Buka file `end_to_end_analytics.ipynb` menggunakan Jupyter Notebook, Jupyter Lab, atau VS Code, lalu jalankan semua sel secara berurutan.

## 📊 Business Insights
Beberapa temuan utama dari proyek ini meliputi:
1. Tingkat retensi pelanggan berbanding lurus dengan durasi berlangganan (*Tenure*). Pelanggan baru berisiko sangat tinggi untuk *churn*.
2. Jenis kontrak (*Month-to-month*) adalah prediktor kuat dari churn dibandingkan dengan kontrak jangka panjang.
3. Layanan tambahan seperti *Fiber Optic* memiliki harga yang lebih mahal dan berkontribusi terhadap tingkat *churn* jika tidak diimbangi dengan *customer experience* yang baik.
