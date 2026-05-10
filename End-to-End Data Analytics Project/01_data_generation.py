import pandas as pd
import numpy as np
import random
import os

def generate_telecom_data(num_records=5000):
    np.random.seed(42)
    random.seed(42)

    customer_ids = [f"CUST-{str(i).zfill(5)}" for i in range(1, num_records + 1)]
    genders = np.random.choice(['Male', 'Female'], size=num_records)
    ages = np.random.randint(18, 75, size=num_records)
    
    # Tenure in months (0 to 72)
    tenures = np.random.randint(0, 73, size=num_records)
    
    contract_types = np.random.choice(['Month-to-month', 'One year', 'Two year'], size=num_records, p=[0.5, 0.3, 0.2])
    
    # Internet Service
    internet_services = np.random.choice(['DSL', 'Fiber optic', 'No'], size=num_records, p=[0.35, 0.45, 0.20])
    
    monthly_charges = []
    total_charges = []
    churn = []

    for i in range(num_records):
        # Base charge
        base = 20
        
        # Add internet charge
        if internet_services[i] == 'DSL':
            base += 30
        elif internet_services[i] == 'Fiber optic':
            base += 50
            
        # Add random variation
        monthly = base + random.uniform(-5, 15)
        monthly_charges.append(round(monthly, 2))
        
        # Total charges is approximately monthly * tenure
        if tenures[i] == 0:
            total = 0.0
        else:
            # add some variation to total
            total = monthly * tenures[i] + random.uniform(-20, 20)
        
        # Sometime total charge is missing or 0
        if random.random() < 0.01: # 1% missing values to simulate real world data
            total_charges.append(np.nan)
        else:
            total_charges.append(max(0, round(total, 2)))

        # Churn probability logic
        churn_prob = 0.1 # base churn prob
        
        if contract_types[i] == 'Month-to-month':
            churn_prob += 0.3
        elif contract_types[i] == 'Two year':
            churn_prob -= 0.08
            
        if internet_services[i] == 'Fiber optic':
            churn_prob += 0.15 # Higher churn for fiber optic (maybe price sensitivity)
            
        if tenures[i] < 6:
            churn_prob += 0.2
        elif tenures[i] > 24:
            churn_prob -= 0.15
            
        if monthly > 70:
            churn_prob += 0.1
            
        churn_prob = max(0.01, min(0.99, churn_prob))
        
        is_churn = 'Yes' if random.random() < churn_prob else 'No'
        churn.append(is_churn)

    # Create DataFrame
    df = pd.DataFrame({
        'CustomerID': customer_ids,
        'Gender': genders,
        'Age': ages,
        'Tenure': tenures,
        'InternetService': internet_services,
        'Contract': contract_types,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'Churn': churn
    })

    return df

if __name__ == "__main__":
    print("Mulai menghasilkan data sintetik untuk pelanggan telekomunikasi...")
    df = generate_telecom_data(5000)
    
    output_path = "telecom_churn_data.csv"
    df.to_csv(output_path, index=False)
    
    print(f"Data berhasil dibuat dengan {len(df)} baris.")
    print(f"Disimpan di: {os.path.abspath(output_path)}")
    print("\nSample Data:")
    print(df.head())
