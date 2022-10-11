class Jednorožec:
    def __init__(self, jmeno, barva, is_alive=False):
        self.jmeno = jmeno
        self.barva = barva
        self.is_alive = is_alive

    def __str__(self):
        return f'{self.jmeno} ma {self.barva} barvu'

    def vypis_informace(self):
        vypis = f'Jmenuji se {self.jmeno} a mam {self.barva} barvu'
        if self.is_alive:
            vypis += 'a je na zivu.'
        else:
            vypis += 'a uz neziju.'
        return vypis


karel = Jednorožec('Karel', 'duhovou', is_alive=True)
print(karel)

lenka = Jednorožec('Lenka','pruhovanou')
print(lenka.vypis_informace())