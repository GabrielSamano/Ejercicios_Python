# Valores Booleanos.

print(5>10);
print(10<20);
print(10==9);

a= 50
b= 35
c= a/b

if c>15:
    print("C is greater than 15")
else:
    print("C is not greater than 15")


# Evaluando valores y variables.

print(bool("Hello"));
print(bool(15));


# Evaluar booleano en una clase.
class wopa():
    def ajolote(self):
        return 0

explorer = wopa
print(bool(explorer));


# Evaluar una funcion.
def Woopa():
    return False

print(Woopa());

def Manati():
    return False
if Manati():
    print("yes!")
else:
    print("No!")