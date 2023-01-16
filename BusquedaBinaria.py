import random
import time

def Busqueda_azar(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def Busqueda_Binaria(lista, objetivo, limiteSuperior=None, limiteInferior=None):
    if limiteInferior is None:
        limiteInferior = 0 # Aqui comienza la lista
    if limiteSuperior is None:
        limiteSuperior = len(lista)-1

    if limiteSuperior < limiteInferior:
        return -1

    punto_medio = (limiteInferior + limiteSuperior) // 2

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif punto_medio < lista[punto_medio]:
        return Busqueda_Binaria(lista, objetivo, limiteInferior, punto_medio-1)
    else:
        return Busqueda_Binaria(lista, objetivo, punto_medio+1, limiteSuperior)
        
         
