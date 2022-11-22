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
            persona="O"
            computadora="X"
            break
        else:
            print("Porfavor elige entre X/O")


def tabla():
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

    

        