base = float(input("mete la base: "))
exponente = int(input("mete el exponente: "))

resultado = 1

for i in range(exponente):
    resultado *= base

print(" resultado:", resultado)
