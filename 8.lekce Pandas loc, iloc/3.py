""" ukol-08: Adopce zvířat

Stáhni si dataset, který obsahuje seznam zvířat k adopci v ZOO Praha. Zdroj dat je Národní katalog otevřených dat.
Data si načti pomocí metody pandas.read_csv(). Pozor, nastav oddělovač na znak středníku. Využij parametr sep.
Seznam se s daty. Kolik má tabulka řádek a sloupců? Jak se sloupce jmenují?
Které zvíře se nachází na záznamu s indexem 34? Vypiš pomocí iloc název tohoto zvířete v češtině i angličtině.

Bonus
V lekci jsme zmínili, že existují i jiné typy indexů, než jen číselný, který sám vyrobí pandas. Například v kontextu souboru se zvířaty se nabízí hned několik sloupců, které bychom mohli využít jako index, které nejsou číselné.
Načti znovu data, ale tentokrát nastav parametr index_col na název sloupce, který obsahuje název zvířete v češtině. Všimni si, že sloupec teď povýší na index a už se nenachází mezi "běžnými" sloupci.
Pomocí <tvoje-promenna>.index.is_unique ověř, zda je nový index unikátní.
Seřazený index je efektivnější a přehlednější. Seřaď index pomocí metody .sort_index(). Bacha, metoda vrátí novou tabulku se seřazeným indexem. Budeš tedy chtít přepsat původní dataframe.
Vyhledej řádek indexovaný názvem "Outloň váhavý". Namísto metody .iloc využij .loc.
Rozsahy fungují podobně jako u číselných indexů. Vyhledej záznamy mezi "Želva Smithova" a "Želva žlutočelá"."""

import pandas

zoo = pandas.read_csv('8.lekce Pandas loc, iloc/adopce-zvirat.csv', sep = ";")
print(zoo)
print(zoo.shape)
# Tabulka má 513 řádků x 6 sloupců
print(zoo.columns)
print(zoo.iloc[33])
print(zoo.iloc[33, [1,2]])

#Bonus

zoo = zoo.set_index('nazev_cz')
print(zoo)
print(zoo.index.is_unique)
# True
zoo1 = zoo.sort_index()
print(zoo1)
print(zoo1.loc["Outloň váhavý"])
print(zoo1.loc["Želva Smithova":"Želva žlutočelá"])