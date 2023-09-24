import pandas
import seaborn
import matplotlib.pyplot as plt
from scipy import stats
import numpy
import statsmodels as sm
import statsmodels.formula.api as smf 

data = pandas.read_csv("house_prices.csv")
# g = seaborn.regplot(data, x="GrLivArea", y="SalePrice", scatter_kws={"s": 1}, line_kws={"color":"r"})
# plt.show()

data["SalePriceZScore"] = numpy.abs(stats.zscore(data['SalePrice']))
data = data[data["SalePriceZScore"] < 3]
# g = seaborn.regplot(data, x="GrLivArea", y="SalePrice", scatter_kws={"s": 1}, line_kws={"color":"r"})
# plt.show()

data["logSalePrice"] = numpy.log(data["SalePrice"])
formula = "logSalePrice ~ GrLivArea"
#formula = "SalePrice ~ GrLivArea"
mod = smf.ols(formula, data)
res = mod.fit()
# print(res.summary())
data["residuals"] = res.resid
data["predictions"] = res.fittedvalues
print(res.summary())
# print(data[["GrLivArea", "SalePrice", "predictions", "residuals"]])
# data["residuals"].plot.kde()
# plt.show()

