class Nemoc:
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        self.jmeno = jmeno
        self.inkubacni_doba = inkubacni_doba
        self.pocet_obeti = pocet_obeti
        self.sireni = sireni

    def __str__(self):
        return f"Jmeno: {self.jmeno}."

    def zmen_pocet_obeti(self, pocet_obeti):
        self.pocet_obeti = pocet_obeti

class Koronavirus(Nemoc):
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        super().__init__(jmeno, inkubacni_doba, pocet_obeti, sireni)
        self.varianty = []
    
    def __str__(self):
        return super().__str__() + f' Varianty: {", ".join(self.varianty)}.'
    
    def pridej_variantu(self, varianta):
        self.varianty.append(varianta)

corona = Koronavirus('Coronavirus', 14, 598645, 'vzduchem')
print(corona)
print(corona.inkubacni_doba) 
print(corona.pocet_obeti)
print(corona.sireni)
corona.pridej_variantu('omikron')
print(corona)
corona.pridej_variantu('delta')
print(corona)
corona.pridej_variantu('alpha')
print(corona)


