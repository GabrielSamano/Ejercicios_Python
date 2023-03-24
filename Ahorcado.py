# En este codigo se muestra un ejemplo de codigo del juego de niños llamado el ahorcado el cual el objetivo es encontrar la palabra escondida
palabra = "ahorcado"
errores = 0
progreso = []

 

for i in range(len(palabra)):
    progreso.append("_ ")
letras_usadas= []
# Dibujando el ahorcado
while errores < 7:
    if errores == 0:
        print("_____")
        print("|   |")
        print("|    ")
        print("|    ")
        print("|    ")
        print("|    ")
        print("|____")
    elif errores == 1:
        print("_____")
        print("|   |")
        print("|   °")
        print("|    ")
        print("|    ")
        print("|    ")
        print("|____")
    elif errores == 2:
        print("_____")
        print("|   |")
        print("|   °")
        print("|   |")
        print("|    ")
        print("|    ")
        print("|____")
    elif errores == 3:
        print("_____")
        print("|   |")
        print("|   °")
        print("|   |")
        print("|  / ")
        print("|    ")
        print("|____")
    elif errores == 4:
        print("_____")
        print("|   |")
        print("|   °")
        print("|   |")
        print("|  / \\")
        print("|    ")
        print("|____")
    elif errores == 5:
        print("_____")
        print("|   |")
        print("|   °")
        print("|  \|")
        print("|  /\\")
        print("|    ")
        print("|____")
    elif errores == 6:
        print("_____")
        print("|   |")
        print("|   °")
        print("|  \|/")
        print("|  /\\")
        print("|    ")
        print("|____")
    break

