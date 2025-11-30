ahorrado = 0

for mes in range(1, 13):
    deposito = float(input(f"mete cantidad ahorrada en el mes {mes}: "))
    ahorrado += deposito

print("Ahorro total :", ahorrado)
