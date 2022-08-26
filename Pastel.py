# creando un Pie con matplot y numpy
# Bases del entrenamiento para tener una buena condicion

from turtle import title
import matplotlib.pyplot as plt
import numpy as np

y = np.array([20,25,20,25,10])

myEtiquetas = ["Trabajar","Aprender","Comer","Descansar","Jugar"]

plt.pie(y, labels=myEtiquetas)
plt.legend(title= "Entrenamiento")
plt.show()