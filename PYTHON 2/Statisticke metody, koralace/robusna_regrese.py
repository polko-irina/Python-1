import pandas
import seaborn
import matplotlib.pyplot as plt
from scipy import stats
import numpy
import statsmodels.api as sm
import statsmodels.formula.api as smf

data = pandas.read_csv("house_prices.csv")
data_x = data[["GrLivArea", "GarageArea"]]
data_x = sm.add_constant(data_x)
mod = sm.RLM(data["SalePrice"], data_x)
res = mod.fit()
print(sum(numpy.abs(res.resid)))