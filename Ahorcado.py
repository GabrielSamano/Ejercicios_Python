# En este codigo se muestra un ejemplo de codigo del juego de niños llamado el ahorcado el cual el objetivo es encontrar la palabra escondida
palabra = "ahorcado"
errores = 0
progreso = []

 

for i in range(len(palabra)):
    progreso.append("_ ")
  
palabra_con_espacio = []
for char in palabra:
    palabra_con_espacio.append(char + " ")
 

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
        print("Perdiste")
    break
    
print(' '.join(progreso))
print("Letras usadas: ", letras_usadas)
print("Elige una letra: ")
letra = input()
if letra in letras_usadas:
    print("Esta letra ya la usaste..")
else:
    letras_usadas.append(letra)

    hay_error = True
    for i in range(len(palabra)):
        if letra == palabra[i]:
            progreso[i] = letra + " "
            hay_error = False
    
    if hay_error:
        errores += 1

    if palabra_con_espacio == progreso:
        print(" " .join(progreso))
        print("Ganaste")
        break

