cantidad = int(input("mete un numero: "))

mayor = 0
menor = 0
igual = 0

for i in range(cantidad):
    num = float(input(f"mete un numero {i+1}: "))

    if num > 0:
        mayor += 1
    elif num < 0:
        menor += 1
    else:
        igual += 1
print("mayor:", mayor)
print("menor:", menor)
print("igual:", igual)