import pandas

znamky = [
    ['Petr', 2],
    ['Roman', 1],
    ['Jitka', 3],
    ['Zuzana', 5],
    ['Ondřej', 2],
    ['Julie', 2],
    ['Karel', 4],
    ['Anna', 1],
    ['Eva', 1]
]

znamky = pandas.DataFrame(znamky, columns=['student', 'znamka'])
print(znamky)

staty_list = znamky.to_numpy().tolist()


nakupy = [
    {"person": "Petr", "item": "Prací prášek", "value": 399},
    {"person": "Ondra", "item": "Savo", "value": 80},
    {"person": "Petr", "item": "Toaletní papír", "value": 65},
    {"person": "Libor", "item": "Pivo", "value": 124},
    {"person": "Petr", "item": "Pytel na odpadky", "value": 75},
    {"person": "Míša", "item": "Utěrky na nádobí", "value": 130},
    {"person": "Ondra", "item": "Toaletní papír", "value": 120},
    {"person": "Míša", "item": "Pečící papír", "value": 30},
    {"person": "Zuzka", "item": "Savo", "value": 80},
    {"person": "Pavla", "item": "Máslo", "value": 50},
    {"person": "Ondra", "item": "Káva", "value": 300}
]

nakupy = pandas.DataFrame(nakupy)
print(nakupy)
