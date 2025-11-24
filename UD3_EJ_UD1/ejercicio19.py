primero = int(input("mETE el primero:"))
segundo = int(input("Mete el segundo:"))
tercero = int(input("Mete el tercero:"))

if primero >= segundo and primero >= tercero:
    mayor = primero
elif segundo >= primero and segundo >= tercero:
    mayor = segundo
else:
    mayor = tercero

if primero <= segundo and primero <= tercero:
    menor = primero
elif segundo <= primero and segundo <= tercero:
    menor = segundo
else:
    menor = tercero

print("El número mayor es:", mayor)
print("El número menor es:", menor)

if primero == segundo == tercero:
    print("Los tres números son iguales.")
elif primero == segundo:
    print("El primero y el segundo  son iguales.")
elif primero == tercero:
    print("El primero y el tercero  son iguales.")
elif segundo == tercero:
    print("El segundo y el tercero son iguales.")
