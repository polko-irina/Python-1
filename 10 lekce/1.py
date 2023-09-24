import requests

file_names = ["u202.csv", "u203.csv", "u302.csv", "studenti.csv", "predsedajici.csv"]

"""for file in file_names:
    url = "https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/agregace-a-spojovani/{}".format( file )
    r = requests.get(url)
    open(file, "wb").write(r.content)
    print(f"File {file} downloaded.") """


import pandas

u202 = pandas.read_csv("u202.csv")
u203 = pandas.read_csv("u203.csv")
u302 = pandas.read_csv("u302.csv")

print(u202)

print(u202['znamka'].isnull())
print(u202['znamka'].notnull())

testovaci_data = u202[u202['znamka'].isnull()]
print(testovaci_data)

print(testovaci_data.dropna(axis=1)) # odstranuje sloupce s hodnotou Nan(axis´ma pouze hodnotu 0 nebo 1. Defoltně je 0)
print(testovaci_data.fillna('Hodnota chybí')) # nahrazuje hodnoty

u202 = pandas.read_csv('u202.csv').dropna()
u203 = pandas.read_csv('u203.csv').dropna()
u302 = pandas.read_csv('u302.csv').dropna()

print(u202)

maturita = pandas.concat([u202, u203, u302], ignore_index=True)

print(maturita)
# print(u202)

u202['mistnost'] = 'u202' # pridat sloupec mistnost s hodnotou u202
u203['mistnost'] = 'u203'
u302['mistnost'] = 'u302'

maturita = pandas.concat([u202, u203, u302], ignore_index=True)
print(maturita)

maturita.to_csv('maturita.csv', index=False)

studenti = pandas.read_csv('studenti.csv')
print(studenti)

propojeny_df = pandas.merge(u202, studenti) # spojování tabulek
print(propojeny_df)
print(propojeny_df.shape)

preds = pandas.read_csv('predsedajici.csv')

novy_propojeny_df = pandas.merge(propojeny_df, preds, on=['den'], how="left")
print(novy_propojeny_df)


novy_propojeny_df[novy_propojeny_df["datum"].isnull()]
preds["den"] = preds["den"].str.strip()
novy_propojeny_df = pandas.merge(propojeny_df, preds, on=['den'], how="left")
print(novy_propojeny_df)

novy_propojeny_df = novy_propojeny_df.rename(columns={'jmeno_x': 'jmeno studenta', 'jmeno_y': 'predseda'})
print(novy_propojeny_df)

print(maturita.groupby('mistnost').count()) # seskupit(agregovat) pres co a jakou funkci (count() v tomto pripadě)

print(maturita.groupby('predmet')['znamka'].mean())
print(maturita.groupby('predmet')[['znamka', 'cisloStudenta']].mean())
