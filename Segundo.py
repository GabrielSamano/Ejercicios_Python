#Segunda parte.

z,y,x=1,2,3
print(x);
print(z);
print(y);

#Imprimir Variables de una lista.
Fruits=["Apple",5,"Orange"];
x,y,z=Fruits
print(x);
print(y);
print(z);

#Imprimir variables juntas.
a="Python";
w="is";
c="awesome";
print(a, w, c);

#Variables Global.
x= "awesome";
def myFunction():
    print("Python is " + x);
myFunction()

#Cambiando variable global
x= "awesome";
def myFunction():
    global x
    x= "Fantastic";
myFunction()
print("Python is " + x);