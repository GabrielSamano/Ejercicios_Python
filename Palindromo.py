# Programa para buscar palindromos 

def isPal(num):
    numString = str(num)
    for i in range(0, int(len(numString)/2+1)):
        if (numString[i] != numString[-i -1]):
            return False
    return True

#Ejemplo de un palindromo para ver si funciona 
if (isPal(1000)):
    print("Si es palindromo")
