# Creacion de un histograma 
# Primero creacion una distribucion de datos normal con numpy

import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(150,50,200)

plt.hist(x)
plt.show()
#print(x)


