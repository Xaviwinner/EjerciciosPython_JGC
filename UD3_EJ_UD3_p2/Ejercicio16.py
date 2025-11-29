contador = 0
nota = 0

while nota != -1:
    nota = int(input("mete tu nota: "))

    if nota == 10:
        contador += 1

if contador > 0:
    print("Hay diez")
else:
    print("No hay diez")
