import pandas

jobs = pandas.read_csv("DataAnalyst.csv")

print(jobs.columns)
print(jobs.iloc[9])

# [2253 rows x 16 columns]

print(jobs.iloc[12:21,1:7])

## Kdyz slupce nejsou vedle sebe
print(jobs.iloc[11:20,[1,7]]) 