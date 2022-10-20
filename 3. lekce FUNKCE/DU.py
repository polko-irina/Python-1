
def delka_cisla(sms):
    sms = sms.replace(" ", "")
    if len(sms) == 9:
        return True
    else:
        return False

# print(delka_cisla('12 34 56 7 8 9'))

def cena_zpravy(massage):
    cena = 3
    a = 1
    b = int((len(massage) / 180))
    a += b
    cena_celkem = a * cena
    return cena_celkem 

# print(len('qwertzuiopúúúúůlkjhgfdsxcvbnm,.lkjhgfdswertzuiopú§ů.qwertzuiopúúúúůlkjhgfdsxcvbnm,.lkjhgfdswertzuiopú§ů.,qwertzuiopúúúúůlkjhgfdsxcvbnm,.lkjhgfdswertzuiopú§ů.qwertzuiopúúúúůlkjhgfdsxcvbnm,.lkjhgfdswertzuiopú§ů.qwertzuiopúúúúůlkjhgfdsxcvbnm,.lkjhgfdswertzuiopú§ů.qwertzuiopúúúúůlkjhgfdsxcvbnm,.lkjhgfdswertzuiopú§ů.,qwertzuiopúúúúůlkjhgfdsxcvbnm,.lkjhgfdswertzuiopú§ů.qwertzuiopúúúúůlkjhgfdsxcvbnm,.lkjhgfdswertzuiopú§ů.'))

cislo = input('Zadej cislo: ')
if delka_cisla(cislo):
    zprava = input('Zadej zpravu: ')
    print(f'Zprava bude stat {cena_zpravy(zprava)} Kc.')
else:
    print('Nespravne cislo.')
