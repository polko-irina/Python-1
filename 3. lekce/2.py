def greet_user(name, age):
    print(f"Ahoj {name} {age}!")

greet_user('Iry', 38)

def sum_a_b(a, b):
    vysledek = a + b
    return vysledek

vysledek = sum_a_b(1, 2)
print(vysledek)


def vypocti_znamku(body, bonusove_body):
    celkove_body = + bonusove_body
    if celkove_body > 20:
        return 1
    return 5

body = int(input('Zadej body: '))
print(vypocti_znamku(body, 30))
print(vypocti_znamku(body))