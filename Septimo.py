# Listas

firstlist= ["Orange","apple",25,True,"Mundo"]
print(firstlist);
print(len(firstlist));
print(type(firstlist));
print(firstlist[1]);
print(firstlist[-2]);
print(firstlist[1:3]);
# Cambiar elementos de la lista.
firstlist[2:3]=["Pencil","Earaser"]
print(firstlist);
# Agregar nuevos elementos.
firstlist.append("Hola")
print(firstlist);
firstlist.insert(1, "Mundo");
print(firstlist);
#combinar listas.
se_list=[1,2,3,4];
firstlist.extend(se_list);
print(firstlist);
#Bucle for en la lista.
list_1= [1,5,4,3,8]
for x in list_1:
    print(x);
#Bucle while en la lista.
gol = ["Hola", "Loop", "Wopa","Eagle"]
i = 0
while i < len(gol):
    print(gol[i])
    i= i + 1

newlis= [x for x in gol if "a" in x];
print(newlis);

#Ordenar las listas.
gol.sort()
print(gol)