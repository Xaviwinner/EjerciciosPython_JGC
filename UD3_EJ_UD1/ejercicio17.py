""" programa que lea dos números y lo visualiza en orden ascendente"""

primero = int(input("Ingrese el primero:"))
segundo = int(input("Ingrese el segundo:"))

if primero > segundo:
    print(segundo,primero)
else:
    print(primero,segundo)