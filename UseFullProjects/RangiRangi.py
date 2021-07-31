'''Barname Baraye Neshoon Dadan Zibaiihaye Ketabkhane matplotlib'''
#AZ
import matplotlib.pyplot as plt
import random as rnd

x = list(range(100))
y = list(map(lambda a : rnd.randrange(100), x))
size = list(map(lambda a : rnd.randrange(100) * 25, x))
color = list(map(lambda a : rnd.randrange(100), x))
colormaps = plt.colormaps()

for i in range(7):
    plt.scatter(x, y,s = size, c = color, alpha = 0.5, cmap = colormaps[y[i] % len(colormaps)])
    plt.colorbar()
    plt.title(colormaps[y[i] % len(colormaps)])
    plt.show()
    plt.close()