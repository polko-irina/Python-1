# 1. Vysvědčení
# Uvažujme vysvědčení, které máme zapsané jako slovník.
# Napiš program, který spočte průměrnou známku ze všech předmětů.
# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

soucet_znamek = 0
for predmet, hodnoceni in school_report.items():
    soucet_znamek += hodnoceni
prumer = soucet_znamek / len(school_report)
print(prumer)

for predmet, hodnoceni in school_report.items():
    if hodnoceni == 1:
        print(predmet)



# 2 Čtenářský deník
# Gustav je vášnivým čtenářem detektivek z našeho nakladatelství a navíc si zapisuje knihy, které přečetl. Níže ve slovníku vidíme, jaké informace si eviduje - název knihy, počet stran a hodnocení od 0 do 10.
# Napiš program, který spočte celkový počet stran, které Gustav přečetl.
# Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8

books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

# Napiš program, který spočte celkový počet stran, které Gustav přečetl.
sum_pages = 0
for book in books:
    sum_pages += book['pages']

# Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.
sum_pages = 0
books_better_than_8 = 0
for book in books:
    sum_pages += book['pages']
    if book['rating'] >= 8:
        books_better_than_8 += 1
print(f'Pocet stran vsech knih: {sum_pages}')
print(f'Pocet knih s hodnocenim alespon 8: {books_better_than_8}')



# 3 Poznávací značky
# V následujícím slovníků je evidence automobilů. Klíčem jsou státní poznávací značky (SPZ) a hodnotou je jméno majitele vozu. Napiš program, který vypíše všechny majitele, jejichž vozidlo je registrováno v Plzeňském kraji, tj. na druhém místě (index 1!) řetězce v klíči je písmeno P.

plates = {"4A2 3000": "František Novák",
    "6P5 4747": "Jana Pilná",
    "3B7 3652": "Jaroslav Sečkár",
    "1P5 5269": "Marta Nováková",
    "37E 1252": "Martina Matušková",
    "2A5 2241": "Jan Král"}

for spz, majitel in plates.items():
    if spz[1] == "P":
        print(majitel)