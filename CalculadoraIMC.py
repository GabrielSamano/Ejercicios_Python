# Calculadora para saber el indice de masa corporal de una persona

peso = float(input("Ingrese su peso en Kg: "))

alturaCm = int(input("Ingrese su altura en cm: "))
alturaM = alturaCm / 100

imc = peso / (alturaM * alturaM)

print("Tu IMC es " + str(imc))

if imc < 20:
  print("Estado de delgadez")
if imc >= 20 and < 26:
  print("Peso Normal")
if imc >= 26 and < 30:
  print("Peso Normal")
if imc >= 30:
  print("Estado de sobrepeso")
