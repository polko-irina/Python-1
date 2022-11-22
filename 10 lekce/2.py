import pandas

studenti1 = pandas.read_csv("studenti1.csv").dropna()
print(studenti1)

studenti2 = pandas.read_csv("studenti2.csv").dropna()
print(studenti2)

st = pandas.concat([studenti1, studenti2], ignore_index=True)
print(st)

prezencni_st = st.groupby('obor')["jméno"].count()
print(prezencni_st)

prezencni_st = st.groupby('obor')["prospěch"].mean()
print(prezencni_st)

jmena = pandas.read_csv('jmena.csv')
print(jmena)

studenti_joined = pandas.merge(st, jmena[['jméno', 'pohlaví']], on='jméno', how='left')
print(studenti_joined)

studenti_joined_all = pandas.merge(st, jmena, on='jméno', how='left')
print(studenti_joined_all)