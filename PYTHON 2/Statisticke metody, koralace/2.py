import pandas
import seaborn
import matplotlib.pyplot as plt

data = pandas.read_csv("house_prices.csv")
seaborn.scatterplot(data=data, x="GrLivArea", y="SalePrice")
# plt.show()

data_vybrane_sloupce = data[["GrLivArea", "SalePrice"]]
print(data_vybrane_sloupce.corr())