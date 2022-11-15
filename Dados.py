from random import*

name1p = input("Ingrese el nombre del primer jugador \n")
name2p = input("Ingrese el nombre del segundo jugador \n")

gameWin1p = 0
gameWin2p = 0

numGame = 1

continueGame = True

while ( gameWin1p < 2 and gameWin2p < 2) and continueGame:
    print("Partida n ", numGame)

    objetivo = randint(1,6)
    print ("EL objetivo es ", objetivo)

    num1P1 = randint(1,6)
    num2P1 = randint(1,6)
    sumP1 = num1P1 + num2P1

    num1P2 = randint(1,6)
    num2P2 = randint(1,6)
    sumP2 = num1P2 + num2P2

    print("EL jugador: ", name1p , " Ha sacado " , num1P1 , " y ", num2P1)
    print("El jugador: ", name2p, " Ha sacado ", num1P2, " y ", num2P2)

    numWinner = 0
    if sumP1 == objetivo:
        numWinner = numWinner + 1
        gameWin1p = gameWin1p + 1

    if sumP2 == objetivo:
        numWinner = numWinner + 1
        gameWin2p = gameWin2p + 1

    if numWinner == 2:
        print("Han ganado los dos")
    elif numWinner == 1:
        if sumP1 == objetivo:
            print("Ha gando el jugador: ", name1p)
        if sumP2 == objetivo:
            print("Ha ganado el jugador: ", name2p)
        else:
            print("No ha ganado nadie")

        continueGame = input("Quiere seguir jugando? (S/N)") == "S"
        numGame = numGame + 1


print("Juego Terminado")
print("Se han jugado ", numGame, " partidas")
