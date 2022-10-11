class Balik :
    def __init__(self, adresa, hmotnost):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = False

    def __str__(self):
        return (f'Na adresu {self.adresa} byl doručen balik o hmotnosti {self.hmotnost}kg.')

balik = Balik('Lidicka', 15.5)
print(balik)
print(balik.hmotnost)
print(balik.adresa)
print(balik.doruceno)

