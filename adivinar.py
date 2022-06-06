import random

def advina_el_numero(x):
    print("===========")
    print("Welcome")
    print("Tienes que adivinar el numero genrado por la computadora")

    numero_aleatorio = random.randint(1, x) # Numeros entre 1 y x

    prediccion = 0

    while prediccion != numero_aleatorio:
        prediccion = int(input(f"adivina entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print("Intentalo otra vez es muy pequeño")
        elif prediccion > numero_aleatorio:
            print("Intentalo otra vez es muy grande")

    print(f"!Felicitaciones adivinaste el numero {numero_aleatorio}")

advina_el_numero(10);

