import pandas
from scipy import stats

data = pandas.read_csv("house_prices.csv")
# res = stats.kendalltau(data["SalePrice"], data["GrLivArea"])
res = stats.shapiro(data["SalePrice"])
print(res)

