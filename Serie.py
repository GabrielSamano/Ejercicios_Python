sum = 0
num1 = 0
num2 = 1

while num2 < 4000000: # Ingresa el rango que tu consideres 
    temp = num1
    num1 = num2
    num2 = num2 + temp
    if (num1 % 2 ==0): # Utiliza los numeros pares 
        sum += num1

print(sum)
    
