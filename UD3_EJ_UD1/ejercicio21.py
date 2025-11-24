negativo = False

print("Mete 100 números :")

for i in range(1, 101):
    numerp = float(input("Mete el número : "))
    if numerp == 0:
        print("El número no puede ser 0. Intente de nuevo.")
        numerp = float(input("Mete el número: "))

    if numerp < 0:
        negativo = True

if negativo:
    print("Se ha leído al menos un número negativo.")
else:
    print("No se leyó ningún número negativo.")
