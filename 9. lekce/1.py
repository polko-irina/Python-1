import requests

url = "https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/zakladni-dotazy/staty.json"
r = requests.get(url) # <Response [200]>
open("staty.json", "wb").write(r.content)

import pandas

staty = pandas.read_json("staty.json")
print(staty)

print(staty.head())

staty = staty.set_index("name")
print(staty.index)

print(staty.loc["Czech Republic", "population"])

print(staty.loc["Czech Republic"])

print(staty.loc[:"Czech Republic"])

print(staty.loc["Czech Republic":])

print(staty.loc[:"Andorra"])
print(staty.loc["Uzbekistan":]) 
print(staty.loc[["Czech Republic","Slovakia"]])
print(staty.loc[["Slovakia","Poland","Germany","Austria"], ["area","population"]])

print(staty.iloc[1:5])

populace = staty["population"]
print(populace.sum())
print(staty["population"].sum())

print(f"Prumer je {populace.mean()}.")
print(f"Minumum je {populace.min()}.")
print(f"Maximum je {populace.max()}.")
print(f"Median je {populace.median()}.")
print(staty["area"].max())
print(populace.describe())
print(staty.describe())

print(staty["population"] < 1000)

pidistaty = staty[staty["population"] < 1000]
print(pidistaty[["population", "area"]])

lidnate_evropske_staty = staty[(staty["population"] > 20000000) & (staty["region"] == "Europe")]
print(lidnate_evropske_staty["population"])

print(staty.query("population > 20000000 and region == 'Europe'"))
print(staty.query("population > 20000000 or region == 'Europe'"))

print(staty[(staty["population"] > 10_000_000_000) | (staty["area"] > 3_000_000)])

print(staty[staty["subregion"].isin(["Western Europe", "Eastern Europe"])])

print(staty[~staty["subregion"].isin(["Western Europe", "Eastern Europe"])])