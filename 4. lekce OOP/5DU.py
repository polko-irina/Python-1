
class Recept:
    def __init__(self, nazev, narocnost, url_adresa):
        self.nazev = nazev
        self.narocnost = narocnost
        self.url_adresa = url_adresa
        self.vyzkouseno = False

    def __repr__(self):
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
tiramisu.zkusit()
print(tiramisu)

babovka = Recept('Babovku', 'lehký', 'www.babovka.com')
print(babovka)


class Kucharka:
    def __init__(self, nazev, autor):
        self.nazev = nazev
        self.autor = autor
        self.recepty = []

    def __str__(self):
        return (f'Kniha {self.nazev} od {self.autor} ma {len(self.recepty)} recepty.')

    def pocet_receptu(self):
        return len(self.recepty)

    def pridej_recept(self, novy_recept):
        self.recepty.append(novy_recept)
        
        # BONUS # 
    def vyzkousene_recepty(self):
        vyzkousene_recepty = []
        for a in self.recepty:
            if a.vyzkouseno:
                vyzkousene_recepty.append(a.nazev)
        return f"Byly vyzkouseny recepty na {', '.join(vyzkousene_recepty)}."
    
dezerty = Kucharka('Dezerty', 'Iryny')
print(dezerty)
dezerty.pridej_recept(muffiny)
dezerty.pridej_recept(tiramisu)
dezerty.pridej_recept(babovka)

pernik = Recept('Pernik', 'hodně slozity', 'www.pernik.com')
dezerty.pridej_recept(pernik)
print(dezerty.pocet_receptu())
print(dezerty)

 # BONUS X
pernik.zkusit()
print(dezerty.vyzkousene_recepty())

