import pandas
# načtení dat
data = pandas.read_csv("titanic.csv")

# vytvoření kontingenční tabulky
titanic_pivot_table = pandas.pivot_table(data, values="Name", index="Sex", columns=["Survived"], aggfunc=len)
print(titanic_pivot_table)

titanic_pivot_table = pandas.pivot_table(data, values="Name", index="Pclass", columns=["Survived"], aggfunc=len)
print(titanic_pivot_table)

titanic_pivot_table = pandas.pivot_table(data, values="Name", index="Sex", columns=["Survived"], aggfunc=len, margins=True)
titanic_pivot_table = titanic_pivot_table.div(titanic_pivot_table.iloc[:,-1], axis=0)
print(titanic_pivot_table)

titanic_pivot_table = pandas.pivot_table(data, values="Name", index="Pclass", columns=["Survived"], aggfunc=len, margins=True)
titanic_pivot_table = titanic_pivot_table.div(titanic_pivot_table.iloc[:,-1], axis=0)
print(titanic_pivot_table)

# děti, teenageři, dospělí a senioři
data["age_group"] = pandas.cut(data["Age"], [0, 12, 20, 60, float("inf")], labels=["children", "teenagers", "adults", "senior citizens"])
titanic_pivot_table = pandas.pivot_table(data, values="Name", index="age_group", columns=["Survived"], aggfunc=len)
print(titanic_pivot_table)