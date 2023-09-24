import pandas
from scipy import stats
import matplotlib.pyplot as plt
data = pandas.read_csv("house_prices.csv")
print(data.head())

print(data["SalePrice"].mean())
print(data["SalePrice"].median())

data_RM = data[data["MSZoning"] == "RM"]
data_RH = data[data["MSZoning"] == "RH"]

print(data_RM["SalePrice"].mean())
print(data_RH["SalePrice"].mean())

print(data_RH["SalePrice"].var())
print(data_RM["SalePrice"].var())

print(data["SalePrice"].quantile(0.1))

print(stats.percentileofscore(data["SalePrice"], 200000))
# data["SalePrice"].hist(bins=25)
data["SalePrice"].plot.kde()
plt.show()
