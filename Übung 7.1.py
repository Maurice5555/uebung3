#Aufgabe 1

import numpy as np
import matplotlib.pyplot as plt

x = np.random.random(1000) * 200 - 100
y = np.random.random(1000) * 200 - 100

plt.scatter(x, y, c=np.random.random(1000))

plt.show()


