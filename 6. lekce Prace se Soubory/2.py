import sys

with open('vykaz.txt', 'r', encoding='utf-8') as file:
    vykaz = file.readlines()

hodiny = ([hod.rstrip() for hod in vykaz])
# mzda = input('Hodinova mzda? ')
mzda = int(sys.argv[1])
celkem_hodin = sum([int(hod) for hod in hodiny])
print(celkem_hodin)
print(mzda)
print(f'Celkova vyplata je: {int{mzda} * celkem_hod}')