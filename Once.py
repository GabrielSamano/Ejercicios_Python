# Array

Cars = ["Ford", "BMW", "Ferrari", "Nissan"]
x = Cars[2]
print(x)

# Clases y objetos.
class MyfirstClass:
    x = 5

x1 = MyfirstClass()
print(x1.x)

class Persona():
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def myFunction(self):
        print("Hello my name is " + self.name)
v1 = Persona("Luis", 24, "Blue")
v1.myFunction()
print(v1.name)
print(v1.age)
print(v1.color)