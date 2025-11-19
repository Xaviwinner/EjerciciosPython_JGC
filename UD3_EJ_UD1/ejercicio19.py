primero = int(input("Ingrese el primero:"))
segundo = int(input("Ingrese el segundo:"))
tercero = int(input("Ingrese el tercero:"))
""" lea dos números y nos diga cual es mayor o si son iguales"""

if primero >= segundo and primero >= tercero:
    mayor = primero
elif segundo >= primero and segundo >= tercero:
    mayor = segundo
else:
    mayor = tercero

# Encontrar el menor
if primero <= segundo and primero <= tercero:
    menor = primero
elif segundo <= primero and segundo <= tercero:
    menor = segundo
else:
    menor = tercero

print("El número mayor es:", mayor)
print("El número menor es:", menor)

# ver si hay iguales
if primero == segundo == tercero:
    print("Los tres números son iguales.")
elif primero == segundo:
    print("El primero y el segundo  son iguales.")
elif primero == tercero:
    print("El primero y el tercero  son iguales.")
elif segundo == tercero:
    print("El segundo y el tercero son iguales.")
