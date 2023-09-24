import pandas
import seaborn
import matplotlib.pyplot as plt

data = pandas.read_csv("house_prices.csv")

data_vybrane_sloupce = data[["LotArea", "SalePrice", "GarageArea"]]
print(data_vybrane_sloupce.corr())
# seaborn.scatterplot(data=data, x="GarageArea", y="LotArea")
# plt.show()

data_lot_area = data[["LotArea", "SalePrice", "GrLivArea"]]
print(data_lot_area.corr())
# seaborn.scatterplot(data=data, x="LotArea", y="SalePrice")
# plt.show()

print(data["GrLivArea"].describe())
print("Kvadratické rozpětí je :", 1775 - 1128)



