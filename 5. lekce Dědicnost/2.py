class Zamestnanec:
    def __init__(self, jmeno, pozice):
        self.jmeno = jmeno
        self.pozice = pozice
        self.pocet_dni_dovolene = 25

    def __str__(self):
        return f'{self.jmeno} pracuje na pozici {self.pozice}. '

    def cerpani_dovolene(self, pocet_dni):
        if pocet_dni <= self.pocet_dni_dovolene:
            self.pocet_dni_dovolene -= pocet_dni
            return f'Zbyva dovolene: {self.pocet_dni_dovolene}'
        else:
            return f'Nemas dostatek dovolene: {self.pocet_dni_dovolene}'

class Brigadnik(Zamestnanec):
    def __init__(self, jmeno, pozice, uvazek):
        super().__init__(jmeno, pozice)
        self.uvazek = uvazek
    
    def __str__(self):
        return super().__str__() + f'Pracuje na {self.uvazek} uvazek.'


frantisek = Zamestnanec('Frantisek', 'Programator')
print(frantisek.cerpani_dovolene(5))
print(frantisek.cerpani_dovolene(15))
print(frantisek.cerpani_dovolene(10))
martin = Brigadnik('Martin', 'brigadnik', 'polovični')
print(martin)