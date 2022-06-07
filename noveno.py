# Senetencia if
a = 550
b = 560
if b > a:
    print("B es mas grande que a")

c = 125
if c > a:
    print("C es mas grande que a")
elif c < b:
    print("C es mas pequeño que b")

d = 150
if d == c:
    print("D y C son iguales");
else:
    print("Son diferentes");

# Bucle while
i = 15
while i < 25:
    print(i)
    i +=1
else:
    print("i Terminó");

# Bucle for

Frutas= {"Orange", "Apple", "Cherry", "Strowberry"}
for x in Frutas:
    print(x)

Dic = ["Car", "Movie", "Fruit"]
Lol = ["Ford", "Spiderman", "Apple"]
for x in Dic:
    for y in Lol:
        print(x, y);