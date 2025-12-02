negativos = 0
positivos = 0

print("Mete 100 números :")

for i in range(1, 101):
    numerp = float(input("Mete el número : "))

    while numerp == 0:
        print("El número no puede ser 0")
        numerp = float(input("Mete el número : "))

    if numerp < 0:
        negativos += 1
    else:
        positivos += 1

print("Cantidad de números negativos:", negativos)
print("Cantidad de números positivos:", positivos)
