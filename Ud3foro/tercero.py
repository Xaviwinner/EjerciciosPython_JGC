n = int(input("mete un número: "))

espacio = " "
asterisco = "*"

for fila in range(n):
    if fila % 2 == 0:
        for i in range(n):
            print(asterisco + espacio, end="")
        print()
    else:
        for i in range(n):
            print(asterisco + espacio * 2, end="")
        print()
