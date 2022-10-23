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


class Kucharka:
    def __init__(self, nazev, autor):
        self.nazev = nazev
        self.autor = autor
        self.recepty = []

    def __str__(self):
        return (f'{self.nazev} od {self.autor} ma {self.recepty.count(Recept)} receptu.')

    def pocet_receptu(self):
        for i in self.recepty:
            self.recepty.count(i)

    def pridej_recept(self, novy_recept):
        self.novy_recept = novy_recept
        for novy_recept in self.recepty:
            self.recepty.append(novy_recept)

dezerty = Kucharka('Dezerty', 'Iryny')
print(dezerty)
dezerty.pridej_recept(muffiny)
dezerty.pridej_recept(tiramisu)
print(dezerty.pocet_receptu())
