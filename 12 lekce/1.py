
import pandas
import matplotlib.pyplot as plt

ucet = pandas.read_csv("12 lekce/ucet.csv")
#print(ucet)

#ucet.plot()
#plt.show()

#ucet.cumsum().plot() # kumulativní suma
#plt.show()

#ucet.plot(kind='bar', color='yellow', grid=True )
#plt.show()

""" Barvy
https://matplotlib.org/stable/tutorials/colors/colors.html

color = "peachpuff" # a named color
color = "#0f0f0f" # RGB hex string
color = (0.1, 0.2, 0.5) # RGB
color = '0' # greyscale, black = 0, white = 1
color = "b" # blue, k = black
color= "C4" # Cn notation
color = "xkcd:crimson """


color = ["red" if value < 0 else "green" for value in ucet["pohyb"]]
ucet["pohyb"].plot(kind = 'bar',
        color = color, 
        width = 0.5,
        grid=True,

        ## Popisky
        ylabel = "Částka v Kč",
        xlabel = "Datum transakce",
        title = "Transakce na účtě"
        )
plt.show()


color = ["#EB5160" if value < 0 else "#91C499" for value in ucet["pohyb"]]
fig, ax = plt.subplots(figsize=(15,7))
print(type(fig))
print(type(ax))

ax.set_title("Pohyby na účtu", fontweight="bold", fontsize = 24)
ax.tick_params(axis="x", labelrotation=45)
ax.set_ylabel("Částka v Kč", color="darkgrey", fontsize = 12)
ax.bar(ucet.index, ucet.pohyb, color = color)
plt.axhline(y=0, color="k", linestyle="--")

## Popisky hodnot v grafu
for i in range(len(ucet.pohyb)):
    plt.annotate(str(ucet.pohyb[i]), 
                xy=(ucet.index[i],
                ucet.pohyb[i]), 
                ha='center', 
                va='bottom')

ax.spines['right'].set_visible(False) # oramovani
ax.spines['left'].set_visible(False) # oramovani
plt.show()

# Style sheets

# https://matplotlib.org/stable/gallery/style_sheets/index.html
# https://towardsdatascience.com/how-to-create-and-use-custom-matplotlib-style-sheet-9393f498063

"""plt.rcParams['figure.figsize'] = [15, 5]
plt.style.use(['dark_background']) # default, grayscale

with plt.xkcd():
    ucet.plot(
        color="blue"
      )
plt.show()"""

# https://www.data-to-viz.com 

muzi = pandas.Series([
    179.3, 183.7, 181.4, 176.0, 183.6, 184.7, 163.4, 180.3,
    167.5, 166.8, 173.5, 172.5, 173.0, 177.6, 176.0, 179.5,
    182.6, 172.0, 183.2, 177.0, 176.2, 175.7, 174.3, 180.3,
    184.9, 171.1, 182.3, 169.7, 181.3, 188.8, 176.8, 159.0,
    180.3, 198.5, 185.8, 191.0, 170.9, 196.0, 183.3, 183.0,
    189.9, 184.8, 184.0, 183.1, 184.0, 190.7, 191.7, 187.8,
    177.5, 177.5, 189.2, 188.4, 195.0, 204.2, 180.2, 181.3,
    178.2, 182.6, 172.1, 175.7, 180.7, 181.2, 165.0, 188.6
])

# muzi.hist()
# plt.show()

# muzi.hist(bins=[
#     150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210
# ], color = "0"
# )
# plt.show()

muzi.plot(kind='box', whis=[0, 100])
#plt.show()

zeny = pandas.Series([
    172.0, 169.0, 166.8, 164.6, 172.7, 171.5, 167.0, 167.0,
    168.3, 184.7, 166.0, 160.0, 168.8, 165.8, 173.5, 163.0,
    168.9, 158.4, 166.4, 169.4, 174.2, 175.6, 167.2, 168.0,
    171.5, 168.8, 168.9, 174.1, 169.0, 170.7, 156.3, 174.8,
    169.1, 161.4, 172.5, 166.1, 171.5, 163.9, 164.5, 169.0,
    168.5, 163.3, 169.5, 167.4, 175.5, 165.0, 166.6, 158.9,
    164.5, 168.7, 161.6, 175.8, 179.0, 167.9, 161.1, 167.6,
    165.9, 165.2, 176.0, 179.4, 160.1, 163.8, 177.7, 160.4
])

vysky = muzi.to_frame(name='muži')
vysky['ženy'] = zeny
vysky.plot(kind='box', whis=[0, 100])
#plt.show()