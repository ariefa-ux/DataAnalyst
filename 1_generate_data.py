import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# Set random seed untuk reproduksibilitas
np.random.seed(42)
random.seed(42)

def generate_ecommerce_data(num_rows=5000):
    print(f"Generating {num_rows} rows of dummy e-commerce data...")
    
    # 1. Menentukan parameter dasar
    categories = {
        'Electronics': ['Smartphone', 'Laptop', 'Headphones', 'Smartwatch', 'Tablet'],
        'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Sneakers', 'Dress'],
        'Home & Garden': ['Blender', 'Coffee Maker', 'Desk Lamp', 'Pillow', 'Plant Pot'],
        'Sports': ['Yoga Mat', 'Dumbbells', 'Running Shoes', 'Water Bottle', 'Tennis Racket']
    }
    
    cities = ['Jakarta', 'Surabaya', 'Bandung', 'Medan', 'Semarang', 'Makassar', 'Denpasar']
    payment_methods = ['Credit Card', 'Bank Transfer', 'E-Wallet', 'Cash on Delivery']
    
    # 2. Membuat data list kosong
    data = []
    
    # Menentukan range tanggal (1 tahun terakhir)
    start_date = datetime(2023, 1, 1)
    
    for i in range(num_rows):
        # Transaction ID
        tx_id = f"TXN-{10000 + i}"
        
        # Random Date within a year
        random_days = random.randint(0, 365)
        tx_date = start_date + timedelta(days=random_days)
        
        # Customer ID
        customer_id = f"CUST-{random.randint(100, 2000)}"
        
        # Product details
        category = random.choice(list(categories.keys()))
        product = random.choice(categories[category])
        
        # Harga dasar (tergantung kategori)
        if category == 'Electronics':
            base_price = random.uniform(1000000, 15000000)
        elif category == 'Clothing':
            base_price = random.uniform(50000, 500000)
        elif category == 'Home & Garden':
            base_price = random.uniform(100000, 2000000)
        else:
            base_price = random.uniform(50000, 1000000)
            
        # Price: Kita akan membuat beberapa nilai outlier (sangat tinggi) secara acak (1% chance)
        if random.random() < 0.01:
            price = base_price * 10 
        else:
            price = base_price
            
        # Quantity (Biasanya 1-5, tapi kita tambahkan nilai negatif untuk simulasi typo/retur (2% chance))
        if random.random() < 0.02:
            quantity = random.randint(-5, -1)
        else:
            quantity = random.randint(1, 5)
            
        # Discount (0 hingga 0.5) - Kita tambahkan missing values (NaN) secara acak (10% chance)
        if random.random() < 0.10:
            discount = np.nan
        else:
            discount = round(random.uniform(0.0, 0.5), 2)
            
        # City - Kita tambahkan missing values (5% chance)
        if random.random() < 0.05:
            city = np.nan
        else:
            city = random.choice(cities)
            
        payment = random.choice(payment_methods)
        
        # Append ke row
        data.append([
            tx_id, tx_date.strftime("%Y-%m-%d"), customer_id, category, 
            product, price, quantity, discount, city, payment
        ])
        
    # 3. Membuat DataFrame
    columns = [
        'Transaction_ID', 'Date', 'Customer_ID', 'Product_Category', 
        'Product_Name', 'Price', 'Quantity', 'Discount', 'City', 'Payment_Method'
    ]
    df = pd.DataFrame(data, columns=columns)
    
    # Format Price menjadi 2 angka di belakang koma
    df['Price'] = df['Price'].round(2)
    
    # 4. Menyimpan ke CSV
    output_filename = 'sales_data.csv'
    df.to_csv(output_filename, index=False)
    print(f"Data successfully generated and saved to '{os.path.abspath(output_filename)}'")
    
    # Menampilkan sedikit info dataset
    print("\nSample Data:")
    print(df.head())
    print(f"\nDataset Shape: {df.shape}")

if __name__ == "__main__":
    generate_ecommerce_data()
