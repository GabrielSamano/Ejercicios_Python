def add(a,b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer))
    
def sub(a,b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer))

def mult(a,b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer))
    
def div(a,b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer))
    
while True:
    print("A. Suma")
    print("B. Resta")
    print("C. Multiplicacion")
    print("D. Division")
    print("E. Exit")

    choice = input("Elige tu opcion: ")
    if choice == "a" or choice == "A":
        print("Suma")
        a = int(input("Ingresa tu primer numero: "))
        b = int(input("Ingresa tu segundo numero: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Resta")
        a = int(input("Ingresa tu primer numero: "))
        b = int(input("Ingresa tu segundo numero: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplicacion")
        a = int(input("Ingresa tu primer numero: "))
        b = int(input("Ingresa tu segundo numero: "))
        mult(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("Ingresa tu primer numero: "))
        b = int(input("Ingresa tu segundo numero: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Fin del programa")
        quit()


