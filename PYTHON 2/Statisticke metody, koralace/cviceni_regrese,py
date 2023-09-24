import pandas
import seaborn
import matplotlib.pyplot as plt
from scipy import stats
import numpy
import statsmodels.api as sm
import statsmodels.formula.api as smf

data = pandas.read_csv("Concrete_Data_Yeh.csv ")
# print(data)

formula = "csMPa ~ slag + flyash"
mod = smf.ols(formula=formula, data=data)
res = mod.fit()
print(res.summary())
