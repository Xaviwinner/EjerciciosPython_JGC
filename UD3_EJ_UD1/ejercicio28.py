suma_pares = 0
suma_impares = 0
for n in range(100, 201):

    if n % 2 == 0:

        suma_pares += n

    else:

        suma_impares += n


print("suma total pare:", suma_pares)


print("suma total impares:", suma_impares)
