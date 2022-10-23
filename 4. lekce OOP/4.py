class Kniha:
    def __init__(self, nazev, pocet_stran, cena):
        self.nazev = nazev
        self.pocet_stran = pocet_stran
        self.cena = cena
    
    def __str__(self):
        return (f'Kniha {self.nazev} ma {self.pocet_stran} a cenu {self.cena}.')

    def sleva(self, procento):
        self.cena = self.cena * (100 - procento) / 100
        return self.cena

kniha = Kniha('Zvirata', 165, 360)
print(kniha)
kniha.sleva(60)
print(kniha)
