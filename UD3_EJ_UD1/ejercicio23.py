positivos = 0
negativos = 0

print("Mete 100 números:")

for i in range(1, 101):
    numerp = float(input("Mete el número: "))

    while numerp == 0:
        print("El número no puede ser 0. Intente de nuevo.")
        numerp = float(input("Mete el número: "))

    if numerp < 0:
        negativos += 1
    else:
        positivos += 1

print("Cantidad de negativos:", negativos)
print("Cantidad de positivos:", positivos)
