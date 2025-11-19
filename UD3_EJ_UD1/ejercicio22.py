negativo = False
positivo=0
negativo=0
print("Ingrese 100 números :")

for i in range(1, 101):
    numerp = float(input("Ingrese el número : "))
    if numerp == 0:
        print("El número no puede ser 0. Intente de nuevo.")
        numerp = float(input("Ingrese el número: "))

    if numerp < 0:
        negativo = True
        negativo+1
    else:
        positivo+1
if negativo:
    print("cantidad de negativos",negativo)
else:
    print("cantidad de positivos"+positivo)
