import sys
sys.modules.keys()

import pandas
print(pandas.__version__)


prvni_dataframe = pandas.DataFrame(columns = ["sloupec1", "sloupec2"])

nakupy = pandas.read_csv('nakupy.csv')
print(nakupy)

nakupy.info()
print(nakupy.shape)

print(nakupy.shape[0])

print(nakupy.columns)

print(nakupy[['Věc', 'Částka v korunách']])

print(nakupy.iloc[3])

print(nakupy.iloc[3:5])

print(nakupy.iloc[:5])

print(nakupy.iloc[5:])

print(nakupy.iloc[-5:])

print(nakupy.head(10))

print(nakupy.tail(2)) # zobrazi konec tabulky

print(nakupy.iloc[1,1])

print(nakupy.iloc[:,2:4])

print(nakupy.iloc[:,2:3])

print(nakupy.iloc[:5,[0,3]]) # vybere pouze sloupec 0 a 3

print(nakupy.iloc[:5,0:3]) # vybere všichni sloupce od 0 do 2