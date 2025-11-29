n = int(input("mete un numero: "))

if n < 0:
    print("tiene que ser positivo")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("El factorial es " + str(factorial))


