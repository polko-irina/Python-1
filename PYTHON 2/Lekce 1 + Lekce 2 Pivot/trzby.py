import matplotlib.pyplot as plt
import pandas

# Načteme data
df_plan = pandas.read_csv("sales_plan.csv")
# komultativni soucet za rok
df_plan["sales_plan_cumsum"] = df_plan.groupby("year")["sales"].cumsum()
# Zobrazíme si hlavičku (prvních 5 řádků)
#print(df_plan.head())
# Zobrazíme si poslednich 5 řádků
#print(df_plan.tail())

print(df_plan)
# nacteni tabulky se skutecnymi trzbami
df_actual = pandas.read_csv("sales_actual.csv")
# seřazeni podle data
df_actual = df_actual.sort_values("date")
# vytvoreni sloupecku date - převod na typ datum a čas
df_actual["date"] = pandas.to_datetime(df_actual["date"])
# vytvořim sloupeček month, kde bude cislo měsice
# ulozeni mesice do samostatne tabulky
df_actual["month"] = df_actual["date"].dt.month
# vytvořim sloupeček year, kde bude cislo roku, ulozeni roku do samostatne tabulky
df_actual["year"] = df_actual["date"].dt.year
print(df_actual.head())
print(df_actual.tail())
# Agregace podle roku a měsice, sectene trzby po mesicich
df_actual_grouped = df_actual.groupby(["year", "month"]).sum()
# kumulativni součet
df_actual_grouped["sales_actual_cumsum"] = df_actual_grouped.groupby("year")["contract_value"].cumsum()
print(df_actual_grouped["sales_actual_cumsum"])
df_merged = pandas.merge(df_plan, df_actual_grouped, on=["month", "year"])
# vypsani vysledku
# print(df_merged)

year = 2022
df_merged_plot = df_merged[df_merged["year"] == year]
df_merged_plot = df_merged_plot.reset_index()
print(df_merged_plot.head())

#df_merged_plot["sales_plan_cumsum"].plot(color="red", title="Skutečné vs plánované tržby")
# čarový graf planovanych tržeb
# plt.show()

#df_merged_plot["period"] = df_merged_plot["month"] + "/" + #df_merged_plot["year"].astype(str)
#df_merged_plot = df_merged_plot.set_index("period")
ax = df_merged_plot["sales_plan_cumsum"].plot(color="red", title ="skutečné versus plánované tržby")
df_merged_plot["sales_actual_cumsum"].plot(kind="bar", ax=ax)
#print(df_merged_plot.head())
df_merged_plot["period"] = df_merged_plot["month"].astype(str) + "/" + df_merged_plot["year"].astype(str)
df_merged_plot = df_merged_plot.set_index("period")
plt.legend(["Plán tržeb", "Skutečné tržby"])
plt.ylabel("UER")
plt.xlabel("Období")
plt.show()
