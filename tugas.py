import pandas as pd

df = pd.read_csv('students.csv')

print("5 Baris Pertama dari DataFrame:")
print(df.head())

print("\nInformasi tentang DataFrame:")
print(df.info())
print("\nDeskripsi Statistik dari DataFrame:")
print(df.describe())

df['Status'] = df['Grade'].apply(lambda x: 'Lulus' if x >= 80 else 'Tidak Lulus')
print(df)

df.to_csv('students_processed.csv', index=False)


rata_rata_nilai = df['Grade'].mean()
print("\nRata-rata nilai Grade mahasiswa:", rata_rata_nilai)

jumlah_per_status = df.groupby('Status').size()
print("\nJumlah mahasiswa berdasarkan Status:")
print(jumlah_per_status)