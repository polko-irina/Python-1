def mult(a, b):
    return a * b

print(mult(10, 6))


def total_price(persons , breakfast = False):
    cena_za_noc = 850
    cena_snidane = 125
    if breakfast:
        return persons * cena_za_noc
    return persons * (cena_za_noc + cena_snidane)

print(total_price(2, True))
print(total_price(3))


def month_of_birth(rodne_cislo):
    rodne_cislo = str(rodne_cislo)
    if int(rodne_cislo[2]) >= 5:
        return int(rodne_cislo[2:4]) - 50
    else:
        return int(rodne_cislo[2:4])

print(month_of_birth(9207054439))
print(month_of_birth(9555125899))


