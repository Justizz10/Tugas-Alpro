import pandas as pd

# Membaca file csv
df = pd.read_csv('data.csv')
print("Data:")
print(df)

# Menampilkan 5 baris pertama
print("\nBaris pertama:")
print(df.head())