books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

for book in books:
    print(book["year"])

for book in books:
    if book['year'] == 2019:
        print(book)

celkovy_profit = 0
for book in books:
    profit = book['sold'] * book['price']
    celkovy_profit += profit
print(celkovy_profit)