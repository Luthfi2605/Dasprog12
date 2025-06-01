import pandas as pd

file_path = r"data_penjualan.xlsx"
data = pd.read_excel(file_path)

data["Total Harga"] = data["Jumlah"] * data["Harga Satuan"]

elektronik_data = data[data["Kategori"] == "Elektronik"]

elektronik_data.to_excel("elektronik.xlsx", index=False)

print(data.head())