import math

num = int(input("mete un numero: "))

if num <= 1:
    print("No es prim")
else:
    es_primo = True
    limite = int(math.sqrt(num))

    for i in range(2, limite + 1):
        if num % i == 0:
            es_primo = False
            break

    if es_primo:
        print(" primo")
    else:
        print("no primo")
