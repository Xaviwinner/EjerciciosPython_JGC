base = float(input("mete la base: "))
exponente = int(input("mete el exponente: "))

if exponente > 0:
    resultado = base ** exponente
elif exponente == 0:
    resultado = 1
else: 
    resultado = 1 / (base ** (-exponente))

print(" resultado :", resultado)
