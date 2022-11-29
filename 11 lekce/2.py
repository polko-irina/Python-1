import re

regex_rodne_cislo = re.compile(r"\d{9,10}")

rezetec = "Moje rodné číslo je 9511121234" # řetězec obsahuje rodné číslo
print(regex_rodne_cislo.match(rezetec))
rezetec = "ahoj"
print(regex_rodne_cislo.match(rezetec))
rezetec_presna_shoda = "9511121234" # řetězec je rodné číslo
retezec_na_zacatku = "9511121234 je moje rodné číslo." # řetězec začína rodným číslem

print(regex_rodne_cislo.fullmatch(rezetec))
print("\nSearch:")
print(regex_rodne_cislo.search(rezetec)) # řetězec obsahuje rodné číslo
print(regex_rodne_cislo.search(rezetec_presna_shoda)) # řetězec je rodné číslo
print(regex_rodne_cislo.search(retezec_na_zacatku)) # řetězec začína rodným číslem

print("\nMatch:")
print(regex_rodne_cislo.match(rezetec)) # řetězec obsahuje rodné číslo
print(regex_rodne_cislo.match(rezetec_presna_shoda)) # řetězec je rodné číslo
print(regex_rodne_cislo.match(retezec_na_zacatku)) # řetězec začína rodným číslem

print("\nFullmatch:")
print(regex_rodne_cislo.fullmatch(rezetec)) # řetězec obsahuje rodné číslo
print(regex_rodne_cislo.fullmatch(rezetec_presna_shoda)) # řetězec je rodné číslo
print(regex_rodne_cislo.fullmatch(retezec_na_zacatku)) # řetězec začína rodným číslem


regularniVyraz = re.compile(r"\d{9,10}")
vstup = input("Zadej rodné číslo: ")
hledani = regularniVyraz.fullmatch(vstup)
if hledani:
    print("Rodné číslo je v pořádku!")
else:
    print("Nesprávné rodné číslo!")


regex_email = re.compile(r"\w+@\w+\.cz")
email = input("Zadej e-mail: ")
hledani = regex_email.fullmatch(email)
if hledani:
    print("E-mail je v pořádku!")
else:
    print("Nesprávný e-mail!")


zapis = """
Zápisy o provedených vyšetřeních:
Pacient 6407156800 trpěl bolestí zad a byl poslán na vyšetření. 
Pacientka 8655057477 přišla na kontrolu po zranění kotníku.
Do ordinace telefonovala pacientka 7752126712, které byl elektronicky vydán recept na Paralen. 
"""
regex_rodne_cislo = re.compile(r"\d{9,10}")
vysledky = regex_rodne_cislo.findall(zapis)
print(vysledky)

anonymni_zapis = regex_rodne_cislo.sub("X", zapis)
print(anonymni_zapis)

anonymni_zapis = regex_rodne_cislo.sub("X", zapis)


Cvičení


