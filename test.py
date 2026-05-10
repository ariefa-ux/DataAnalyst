import pandas as pd

# fungsi
def read_df(path):
    return pd.read_csv(path)

data_s = read_df("sales_data.csv")
print(data_s.head())

data_f = read_df("finance_data.csv")
print(data_f.head())

