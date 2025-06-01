import pandas as pd

file_path = r"data_penjualan.xlsx"
data = pd.read_excel(file_path)

data["Total Harga"] = data["Jumlah"] * data["Harga Satuan"]

sorted_data = data.sort_values(by="Total Harga", ascending=False)
sorted_data.to_excel("data_penjualan_terurut.xlsx", index=False)

print(data.head())