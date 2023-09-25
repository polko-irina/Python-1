import pandas

studenti1 = pandas.read_csv("10 lekce/studenti1.csv").dropna()
print(studenti1)

studenti2 = pandas.read_csv("10 lekce/studenti2.csv").dropna()
print(studenti2)

st = pandas.concat([studenti1, studenti2], ignore_index=True)
print(st)

print(st.groupby('obor')["jméno"].count())

print(st.groupby('obor')["prospěch"].mean())

jmena = pandas.read_csv('10 lekce/jmena.csv')
print(jmena)

studenti_joined = pandas.merge(st, jmena[['jméno', 'pohlaví']], on='jméno', how='left')
print(studenti_joined)

studenti_joined_all = pandas.merge(st, jmena, on='jméno', how='left')
print(studenti_joined_all)