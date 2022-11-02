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
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni, ):
        super().__init__(jmeno, inkubacni_doba, pocet_obeti, sireni)
        self.varianty = []
    
    def __str__(self):
        return super().__str__() + f' Varianty: {", ".join(self.varianty)}.'
    
    def pridej_variantu(self, varianta):
        for varianta in self.varianty: 
            self.varianty.append(varianta)

corona = Koronavirus('Coronavirus', 10, 1000, 'vzduchem')
#corona = Koronavirus('Coronavirus', []) # melo by fungovat stejne jako predchozi radek
print(corona) # 'Jmeno: Coronavirus (zadne nalezene varianty)'
print(corona.pocet_obeti) # nejake cislo ktere se da menit pomoci metody zmen_pocet_obeti() - muze byt nacatku nula nebo cislo ktere si zvolite pri vytvoreni objektu
print(corona.sireni) # 'vzduchem' -- muzete reprezentovat i cislem
print(corona.inkubacni_doba) # 12 -- je mi jedno jake cislo - pevne dane ve volani super().__init__(...)
corona.pridej_varianu('omikron')
corona.pridej_varianu('delta')
print(corona) # 'Jmeno: Coronavirus (varianty: omikron, delta)'
corona.pridej_varianu('alpha')
print(corona) # 'Jmeno: Coronavirus (varianty: omikron, delta, alpha)'


