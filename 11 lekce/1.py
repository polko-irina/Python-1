Vítejte ve Směnárně Na Růžku!
Kurzy měn pro 19. 12. 2020 jsou:

1 €     = 26.35 Kč
1 $     = 21.76 Kč
1 £     = 28.78 Kč
1 DKK   =  3.54 Kč
100 INR = 29.43 Kč

Neúčtujeme žádné poplatky.


Mezi metaznaky patří:
\ ^ $ . [ ] | ( ) ? * + { }


Zápis	Význam
.	libovolný znak
[ ]	jeden z uvedených znaků
[^ ]	jeden z neuvedených znaků


Zápis	Význam
[1-5]	libovolný znak z rozsahu 1, 2, 3, 4, 5
[A-Z ]	všechna velká písmena
[a-z ]	všechna malá písmena
[a-c ]	všechna malá písmena z rozsahu a, b, c


Kvantifikátor	Počet opakování
?	minimálně 0krát, maximálně 1krát
*	minimálně 0krát (maximálně neomezeno)
+	minimálně 1krát (maximálně neomezeno)
{n}	právě nkrát
{m,n}	minimálně mkrát, maximálně nkrát
{m,}	minimálně mkrát (maximálně neomezeno)


Zápis	Význam
\d	číslice 0-9
\D	jakýkoliv znak kromě číslic 0-9
\w	znaky „slova” (ekvivalentní zápisu [a-zA-Z0-9_])
\W	jakýkoliv znak kromě znaků „slova” (ekvivalentní zápisu [^a-zA-Z0-9_])
\s	„bílé” znaky (mezera, tabulátor, znaky pro zalomení řádků)
\S	jakýkoliv znak kromě „bílých” znaků

Znak	Význam
^	začátek řetězce (textu v němž se vyhledává)
$	konec řetězce (textu v němž se vyhledává)
|	nebo --> sobota|neděle
()	opakování určité sekvence znaků


Cvičení 1

\d{0,6}-?\d{6,10}/\d{4}

Cvičení 2

\d{0,6}-?[12]\d{5,9}/2100

Cvičení 3

\d[ A|B|C|E|H|J|K|L|M|P|S|T|U|Z]\w \d{4}