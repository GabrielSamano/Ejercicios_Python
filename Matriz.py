from random import *
fila = 3
columna = 3

a = [[randint (1,1000) for i in range (fila)] for j in range (columna)]

for f in a:
  print(f)
  
c = int (input("Que columna quiere ver"))

b = []

for f in (len(a)):
  b.append(a[f][c])
  
  
print (f)
