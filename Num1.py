import numpy as np
# Creacion de Matrices con Numpy
arr = np.array([1,2,3,4,5]);

print(arr)
print(type(arr))

# Matrices 0-D
rar = np.array(42)
print(rar)
print(rar.ndim)
# Matrices 1-D
r2 = np.array([1,2,3,4,5])
print(r2)
print(r2.ndim)
# Matrices 2-D
r3 = np.array([[1,2,3],[4,5,6]])
print(r3)
print(r3.ndim)
# Matriz 3-D
r5 = np.array([[[1,2,3,4],[1,5,4,7]],[[6,4,8,9],[3,7,6,4]]])
print(r5)
print(r5.ndim)

# Crear matriz

ar = np.array([10,11,12,13], ndmin=5)
print(ar)
print('Numero de dimensiones: ', ar.ndim)

# Forma de la matriz

print(rar.shape)
print(r2.shape)
print(r3.shape)
print(r5.shape)
print(ar.shape)

# Remodelacion de 1-D a 2-D
m1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newr2 = m1.reshape(4, 3)
print(newr2)

# Remodelacion de 1-D a 3-D

newr3 = m1.reshape(2,3,2)
print(newr3)


