
import pandas

jmena = pandas.read_csv('9. lekce/jmena.csv')
print(jmena)

jmena = jmena.set_index("jméno")
print(jmena)

print(jmena.loc['Jiří'])
print(jmena.loc[['Martin','Zuzana','Josef']])

print(jmena.sort_values('četnost').loc[: 'Martin'])

print(jmena.sort_index().loc['Martim': 'Tereza'])

print(jmena.sort_index().loc['Libor': , ['věk', 'původ']])

cols = jmena.columns[1:]
print(cols)

print(jmena['věk'] > 60)
