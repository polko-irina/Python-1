class Zamestnanec:
    def __init__(self, jmeno, pozice, zkusebni_doba):
        self.jmeno = jmeno
        self.pozice = pozice
        self.zkusebni_doba = zkusebni_doba

    def __str__(self):
        vypis = f"{self.jmeno} pracuje na pozici {self.pozice}."
        if self.zkusebni_doba:
            return vypis + ' Je ve zkušební době.'
        return vypis + ' Neni ve zkušební době.'

frantisek = Zamestnanec("František Novák", "konstruktér", False)
print(frantisek)