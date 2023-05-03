# Aufgabe 2

import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return np.exp(-x**2) * np.sin(y)

x_koord = np.linspace(-5, 5, 50)
y_koord = np.linspace(-5, 5, 50)

X, Y = np.meshgrid(x_koord, y_koord)

Z = f(X, Y)

plt.pcolormesh(X, Y, Z)
plt.show()
