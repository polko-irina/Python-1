
def delka_cisla(sms):
    sms = str(sms)
    if int(sms[0:9]) :
        return(int(sms))
    else:
        return('neplatne cislo')

print(delka_cisla(str(123456789)))

# def cena_zpravy(cena, znaky):
#    cena = 3
#    zapocete_znaky = 180 * cena
#    if znaky >= 180
#       return zapocete_znaky
#
# cena_zpravy (3, 250)
