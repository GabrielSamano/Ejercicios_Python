import time
import random
import os

def iniciar_juego():
    print("Bienvenido al juego del Gato")
    time.sleep(1)
    while True:
        ficha = input("Seleccione X / O\n")
        ficha = ficha.upper()
        if ficha =="X":
            persona = "X"
            computadora = "O"
            break
        elif ficha == "O":
            persona ="O"
            computadora="X"
            break
        else:
            print("Porfavor elige entre X/O")


def tabla(matriz):
    print("GAto")
    print()
    print("     |       |     ")
    print("1   {} 2   {} 3  {}".format(matriz[0],matriz[1],matriz[2]))
    print("     |       |     ")
    print("-------------------")
    print("     |       |     ")
    print("4   {} 5   {} 6  {}".format(matriz[3],matriz[4],matriz[5]))
    print("     |       |     ")
    print("-------------------")
    print("     |       |     ")
    print("7   {} 8   {} 9  {}".format(matriz[6],matriz[7],matriz[8]))
    print("     |       |     ")

def empate(matriz):
    empate= True
    i=0
    while(empate== True and i<9):
        if matriz[i]== " ":
            empate= False
            i = i+1
        
        return empate

def victoria(matriz):
    if(matriz[0]==matriz[1]==matriz[2]!=" " or matriz[3]==matriz[4]==matriz[5]!=" " or matriz[6]==matriz[7]==matriz[8]!=" "
        or matriz[0]==matriz[3]==matriz[6]!=" " or matriz[1]==matriz[4]==matriz[7]!=" " or matriz[2]==matriz[5]==matriz[8]!=" " or
        matriz[0]==matriz[4]==matriz[8]!=" " or matriz[2]==matriz[4]==matriz[6]!=" "):
        return True
    else:
        return False

def movimiento_jugador(matriz):
    while True:
        posiciones=[1,2,3,4,5,6,7,8,9]
        casilla=int(input("Seleccione una casilla: "))
        if casilla not in posiciones:
            print("Casilla no disponible")
        else:
            if matriz[matriz-1]==" ":
                matriz[matriz-1]==persona
                break
            else:
                print("Casilla no disponible")


def movimiento_ordenador():
    posiciones=[0,2,3,4,5,6,7,8,]
    casilla=9
    parar=False

    for i in posiciones:
        copia=list(matriz)
        if copia[i]==" ":
            copia[i]=computadora 
            if victoria(copia)==True:
                casilla=i

    if casilla==9:
        for j in posiciones:
            if copia[i]==" ":
                copia[i]=persona
                if victoria(copia)==True:
                    casilla=j

    if casilla==9:
        while(not parar):
            casilla=random.randint(0,8)
            if matriz[casilla]==" ":
                parar=True
    matriz[casilla]=computadora 

    while True:

        matriz=[" "]*9
        os.system("cls")
        persona,computadora = iniciar_juego()
        partida=True
        ganador=0

        while partida:
            ganador=ganador+1
            os.system("cls")
            tabla()


            if victoria(matriz):
                if ganador%2==0:
                    print("Gana el jugador")
                    print("Acaba el juego")
                    print("\n Reiniciando el juego")
                    time.sleep(5)
                    partida=False
                else:
                    print("Gana el ordenador")
                    print("Acaba el juego")
                    print("\n Reiniciando el juego")
                    time.sleep(5)
                    partida=False
            elif empate(matriz):
                print("Empate")
                print("Acaba el juego")
                print("\n Reiniciando el juego")
                time.sleep(5)
                partida=False
            elif ganador%2==0:
                print("EL ordenador esta pensando")
                time.sleep(2)
                movimiento_ordenador()
            else:
                movimiento_jugador()
                print("jugador pensando")
                time.sleep(2)

    

        
