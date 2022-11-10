# Modificar los String.

# Convertir en Mayusculas
a= "Hola Mundo"
print(a.upper());

# Convertir en Minusculas
a= "HOLA Mundo"
print(a.lower());

#Eliminar espacios.
a= "Hola,Mundo! "
print(a.strip());

#Reemplazar texto.
a= "Hola Mundo"
print(a.replace("H","J"));

#Dividir string.
a= "Hola, Mundo"
print(a.split(","));

#Concatenacion.
a= " Hola Mundo "
b= " Python es asombroso "
c= a + b
print(c);

#Combinar formatos de texto.
hola= "Saludos a todo desde el año {}"
year= 2022
print(hola.format(year));

#Caracteres de escape.
saludo= "We are the so-called \"Vikings\" from the north."
print(saludo);
