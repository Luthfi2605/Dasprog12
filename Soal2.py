import pandas as pd

file_path = r"data_penjualan.xlsx"
data = pd.read_excel(file_path)

data["Total Harga"] = data["Jumlah"] * data["Harga Satuan"]

print(data.head())