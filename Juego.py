import random

def juego():
    usuario = input("Escoge una opcion: '1' para piedra, '2' para papel, '3' para tijera.\n").lower()
    computadora = random.choice(["1, 2, 3"])

    if usuario == computadora:
        return '!Empate!'

    if gano_el_jugador(usuario, computadora):
        return 'Ganaste'

    return 'Perdiste'

def gano_el_jugador(jugador, oponente):
    if ((jugador == '1' and oponente == '3')
        or (jugador == '3' and oponente == '2')
        or (jugador == '2' and oponente == '1')):
        return True
    else:
        return False

print(juego())

