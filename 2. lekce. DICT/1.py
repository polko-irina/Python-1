sales = {
    "A": 4165,
    "B": 5681,
    "C": 2565,
}

for book in sales:
    print(book)

for book in sales.values():
    print(book)

for book in sales.items():
    print(book)

for key, value in sales.items():
    print(f'Klič {key} -- {value}')
