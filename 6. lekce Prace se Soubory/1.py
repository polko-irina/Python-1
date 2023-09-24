with open('mereni.txt', 'r', encoding='utf-8') as file:
    radky = file.readlines()  
    file.readline() # proviryty cy vidkrytyj soubor

#for radek in radky:
#    print(radek.replace('\n', ''))

radky = [radek.split('\t') for radek in radky]
print(radky)
radky = [[radek[0], float(radek[1])] for radek in radky]
print(radky)

radky_bez_newline = [radek.replace('\n', '').replace('\t', ' ') for radek in radky]
print(radky_bez_newline)

# radky_bez_newline = [radek.strip() for radek in radky]
# print(radky_bez_newline)