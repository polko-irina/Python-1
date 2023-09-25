import pandas

df = pandas.read_csv("11 lekce/zpravy.csv", sep=";")
print(df)

df["obsahuje_rodne_cislo"] = df["zapis"].str.contains(r"\d{9,10}")
print(df)
df["pocet_rodnych_cisel"] = df["zapis"].str.count(r"\d{9,10}")
print(df)
df["rodna_cisla"] = df["zapis"].str.findall(r"\d{9,10}")
df["anonymni_zapis"] = df["zapis"].str.replace(r"\d{9,10}", "XXX")
print(df)
df["datum_ok"] = df["datum"].str.fullmatch(r"\d{4}-\d{2}-\d{1,2}")
df["datum_ok_cast"] = df["datum"].str.fullmatch(r"\d{4}")
print(df)