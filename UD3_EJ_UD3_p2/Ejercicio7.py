negativo = 0

for i in range(1, 101):
    numero = int(input(f"mete el número {i}: "))

    if numero < 0:
        negativo += 1

print("ha habido un total de " + str(negativo) + " números negativos")
