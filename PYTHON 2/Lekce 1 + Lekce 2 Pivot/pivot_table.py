import pandas
df_actual = pandas.read_csv("sales_actual.csv")
#df_actual["contract_value"] = df_actual["contract_value"] / 1_000_000
df_actual_pivot = pandas.pivot_table(data=df_actual, index="country", columns="sales_manager", values="contract_value", aggfunc=sum, fill_value=0, margins=True)
df_actual_pivot = df_actual_pivot.div(df_actual_pivot.iloc[-1, :], axis=1)
print(df_actual_pivot)
df_actual["group"] = pandas.cut(df_actual["contract_value"], [0, 300_000, 1_000_000, float("inf")], labels=["small", "medium", "big"])
print(df_actual)