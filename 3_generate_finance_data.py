import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# Set random seed untuk reproduksibilitas
np.random.seed(42)
random.seed(42)

def generate_finance_data(num_rows=5000):
    print(f"Generating {num_rows} rows of dummy finance/banking data...")
    
    # 1. Menentukan parameter dasar
    account_types = ['Savings', 'Checking', 'Credit Card', 'Investment']
    
    # Kategori transaksi berdasarkan tipe
    categories = {
        'Income': ['Salary', 'Bonus', 'Investment Return', 'Freelance', 'Gift'],
        'Expense': ['Rent', 'Groceries', 'Utilities', 'Transportation', 'Dining Out', 
                    'Entertainment', 'Healthcare', 'Insurance', 'Shopping', 'Education'],
        'Transfer': ['Internal Transfer', 'External Transfer']
    }
    
    transaction_types = list(categories.keys())
    cities = ['Jakarta', 'Surabaya', 'Bandung', 'Medan', 'Semarang', 'Makassar', 'Denpasar']
    currencies = ['IDR']
    
    # 2. Membuat data list kosong
    data = []
    
    # Menentukan range tanggal (1 tahun terakhir)
    start_date = datetime(2023, 1, 1)
    
    # Inisialisasi saldo awal untuk beberapa customer (simulasi)
    customer_balances = {f"CUST-{100 + i}": random.uniform(5000000, 50000000) for i in range(200)}
    
    for i in range(num_rows):
        # Transaction ID
        tx_id = f"FIN-{20000 + i}"
        
        # Random Date within a year
        random_days = random.randint(0, 365)
        tx_date = start_date + timedelta(days=random_days)
        
        # Customer ID
        cust_id = random.choice(list(customer_balances.keys()))
        
        # Account Type
        account_type = random.choice(account_types)
        
        # Transaction Type (Expense lebih sering dibanding Income)
        tx_type = random.choices(transaction_types, weights=[20, 70, 10])[0]
        
        # Category berdasarkan tipe
        category = random.choice(categories[tx_type])
        
        # Amount (tergantung kategori)
        if category == 'Salary':
            amount = random.uniform(5000000, 20000000)
        elif category == 'Rent':
            amount = random.uniform(1500000, 5000000)
        elif category in ['Groceries', 'Dining Out', 'Transportation']:
            amount = random.uniform(50000, 500000)
        elif category == 'Investment Return':
            amount = random.uniform(100000, 2000000)
        else:
            amount = random.uniform(10000, 1000000)
            
        # Tanda amount: Expense & Transfer Out biasanya negatif (tapi di finance data sering dipisah kolom)
        # Di sini kita simpan sebagai nilai absolut, tapi tipenya jelas
        
        # Simulasi Outliers (1% transaksi sangat besar)
        if random.random() < 0.01:
            amount = amount * 15
            
        # City/Location - Missing values (3% chance)
        if random.random() < 0.03:
            location = np.nan
        else:
            location = random.choice(cities)
            
        # Description
        description = f"{tx_type} for {category} at {location}" if pd.notnull(location) else f"{tx_type} for {category}"
        
        # Update Balance (Simulasi sederhana)
        if tx_type == 'Income':
            customer_balances[cust_id] += amount
        else:
            customer_balances[cust_id] -= amount
            
        balance_after = customer_balances[cust_id]
        
        # Append ke row
        data.append([
            tx_id, tx_date.strftime("%Y-%m-%d"), cust_id, account_type,
            tx_type, category, round(amount, 2), currencies[0], 
            description, location, round(balance_after, 2)
        ])
        
    # 3. Membuat DataFrame
    columns = [
        'Transaction_ID', 'Date', 'Customer_ID', 'Account_Type', 
        'Transaction_Type', 'Category', 'Amount', 'Currency', 
        'Description', 'Location', 'Balance_After'
    ]
    df = pd.DataFrame(data, columns=columns)
    
    # 4. Menyimpan ke CSV
    output_filename = 'finance_data.csv'
    df.to_csv(output_filename, index=False)
    print(f"Finance data successfully generated and saved to '{os.path.abspath(output_filename)}'")
    
    # Menampilkan sedikit info dataset
    print("\nSample Data:")
    print(df.head())
    print(f"\nDataset Shape: {df.shape}")
    print("\nColumn Info:")
    print(df.dtypes)

if __name__ == "__main__":
    generate_finance_data()
