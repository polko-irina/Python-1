class Jednorožec:
    def vypis_informace(self):
        return f'Jmenuji se {self.jmeno} a mam {self.barva} barvu.'


karel = Jednorožec()
karel.jmeno = 'Karel'
karel.barva = 'duhovou'

lenka = Jednorožec()
lenka.jmeno = 'Lenka'
lenka.barva = 'pruhovanou'

print(karel.vypis_informace())
print(lenka.vypis_informace())