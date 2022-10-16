
def delka_cisla(sms):
    sms = str(sms)
    if int(sms[0:9]) :
        return(int(sms))
    else:
        return('neplatne cislo')

print(delka_cisla(str(123456789)))


# def cena_zpravy(cena, znaky):
#    cena = 3
#    znaky = 180
#    zapocete180 = 180 * 3
#    if znaky >= 180
#       return 180 * 3
###    cena_zpravy ()
