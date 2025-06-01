import pandas as pd

file_path = r"data_penjualan.xlsx"
data = pd.read_excel(file_path)

data["Total Harga"] = data["Jumlah"] * data["Harga Satuan"]

rekap_data = data.groupby("Kategori").agg({"Total Harga": "sum"}).reset_index()
rekap_data.columns = ["Kategori", "Total pendapatan"]

print(rekap_data)