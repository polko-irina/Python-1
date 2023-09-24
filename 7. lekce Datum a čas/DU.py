""" Vytvoř program na prodej vstupenek do letního kina. Ceny vstupenek jsou v tabulce níže.

Datum	Cena
1. 7. 2021 - 10. 8. 2021	250 Kč
11. 8. 2021 - 31. 8. 2021	180 Kč
Mimo tato data je středisko zavřené.

Tvůj program se nejprve zeptá uživatele na datum a počet osob, pro které uživatel chce vstupenky koupit. Uživatel zadá datum ve středoevropském formátu. Převeď řetězec zadaný uživatelem na datum pomocí funkce datetime.strptime().

Pokud by uživatel zadal příjezd mimo otevírací dobu, vypiš, že letní kino je v té době uzavřené. Pokud je letní kino otevřené, spočítej a vypiš cenu za vstupenky.

Data lze porovnávat pomocí známých operátorů <, >, <=, >=, ==, !=. Tyto operátory můžeš použít v podmínce if. Níže vidíš příklad porovnání dvou dat. Program vypíše text "Druhá událost se stala po první události".
prvni_udalost = datetime(2021, 7, 1)
druha_udalost = datetime(2021, 7, 3)
if prvni_datum < druhe_datum:
    print("Druhá událost se stala po první události") """

import datetime

from datetime import datetime, timedelta, date

datum = datetime.strptime(input("Datum vstupenky? "), "%d.%m.%Y")
# print(datum)
prvni_datum = datetime(2021, 7, 1)
druhy_datum = datetime(2021, 8, 10)
treti_datum = datetime(2021, 8, 11)
ctvyrty_datum = datetime(2021, 8, 31)

if prvni_datum <= datum <= ctvyrty_datum:
    pocet_osob = int(input("Počet osob? "))
    if prvni_datum <= datum <= druhy_datum:
        cena_vstupenky = pocet_osob * 250
    elif treti_datum <= datum <= ctvyrty_datum:
        cena_vstupenky = pocet_osob * 180
    print(f"Cena vstupenky je: {cena_vstupenky} Kč.")
else:
    print("Letní kino je v této době uzavřené.")