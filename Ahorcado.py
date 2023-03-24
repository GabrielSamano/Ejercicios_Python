# En este codigo se muestra un ejemplo de codigo del juego de niños llamado el ahorcado el cual el objetivo es encontrar la palabra escondida
palabra = "ahorcado"
errores = 0
progreso = []

# Prueba con un ciclo for 

for i in range(len(palabra)):
    progreso.append("_ ")

print(progreso)
