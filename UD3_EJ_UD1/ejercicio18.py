""" lea dos números y nos diga cual es mayor o si son iguales"""


primero = int(input("Ingrese el primero:"))
segundo = int(input("Ingrese el segundo:"))

if primero > segundo:
    print("el primero es mayor")
elif segundo > primero:
        print("el segundo es mayor")

else:
    print("son iguales")

