#Conversion de Numeros
#Numero random
import random

print(random.randrange(1, 10))


x= 1
y= 2.65
z= 5j
#Numero entero a flotante
a = float(x);
#Numero flotante a entero
b = int(y);
#Numero entero a complejo
c = complex(x);

print(a);
print(b);
print(c);

print(type(a));
print(type(b));
print(type(c));

#casting python.
# Primer caso int
x= int(5);   # x seria 5
y= int(4.5);  # y seria 4
z= int("3");  # z seria 3

print(x,y,z);

# segundo caso float
x= float(1);  # x seria 1.0
y= float(2.5);  # y seria 2.5
z= float("3");  # z seria 3.0
w= float("3.2");  # w seria 3.2

print(x,y,z,w);

# tercer caso str

x= str("s1");
y= str("2");
z= str("5.5");

print(x,y,z);