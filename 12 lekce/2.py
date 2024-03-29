import pandas
import matplotlib.pyplot as plt


kostky = pandas.read_csv("12 lekce/kostky.csv")
# print(kostky)

# kostky.hist()
# plt.show()


callcentrum = pandas.read_csv("12 lekce/callcentrum.csv")
callcentrum = callcentrum["hodnota"].str.split(':', expand=True).astype(int)
# print(callcentrum)

callcentrum['cas'] = callcentrum[0] * 60 + callcentrum[1]
callcentrum_graf = callcentrum['cas']

callcentrum_graf.plot(kind='box', color="red")
plt.show()
