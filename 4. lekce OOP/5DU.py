
class Recept:
    def __init__(self, nazev, narocnost, url_adresa):
        self.nazev = nazev
        self.narocnost = narocnost
        self.url_adresa = url_adresa
        self.vyzkouseno = False

    def __str__(self):
        vypis = (f'Recept pro {self.nazev} najdete na strance {self.url_adresa}, postup je {self.narocnost} ')
        if self.vyzkouseno:
            return vypis + 'a již byl vyzkoušen.'
        return vypis + 'a zatim nebyl vyzkoušen.'

    def zmen_narocnost(self, nova_hodnota):
        self.narocnost = nova_hodnota

    def zkusit(self):
        self.vyzkouseno = True

muffiny = Recept('Muffiny', 'lehky', 'www.muffiny.com')
muffiny.zmen_narocnost('složity')
muffiny.zkusit()
print(muffiny)

tiramisu = Recept('Tiramisu', 'mirně složity', 'www.tiramisu.com')
print(tiramisu)

babovka = Recept('Babovku', 'lehký', 'www.babovka.com')
print(babovka)

class Kucharka:
    def __init__(self, nazev, autor):
        self.nazev = nazev
        self.autor = autor
        self.recepty = []
        self.vyzkouseno = False


    def __str__(self):
        return (f'{self.nazev} od {self.autor} ma {len(self.recepty)} receptu.')

    def pocet_receptu(self):
        return len(self.recepty)

    def pridej_recept(self, novy_recept):
        self.recepty.append(novy_recept)
        
    def vyzkousene_recepty(self):
        vyzkousene_recepty = []
        # if 
        #vyzkousene_recepty.append()
        return vyzkousene_recepty
        
dezerty = Kucharka('Dezerty', 'Iryny')
print(dezerty)
dezerty.pridej_recept(muffiny)
dezerty.pridej_recept(tiramisu)
dezerty.pridej_recept(babovka)
print(dezerty.pocet_receptu())

pernik = Recept('Pernik', 'hodně slozity', 'www.pernik.com')
dezerty.pridej_recept(pernik)
print(dezerty.pocet_receptu())

# Bonus 
print(dezerty.vyzkousene_recepty())
pernik.zkusit()
print(pernik)
print(dezerty.vyzkousene_recepty())

