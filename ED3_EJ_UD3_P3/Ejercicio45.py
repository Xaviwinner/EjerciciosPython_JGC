while True:
    inferior = int(input(" límite inferior: "))
    superior = int(input(" límite superior: "))

    if inferior < superior:
        break
    else:
        print("El límite inferior debe ser menor que el superior.")

suma_dentro = 0
fuera = 0
igual_limite = False

print("mete números :")

while True:
    num = int(input("Número: "))

    if num == 0:
        break

    if num == inferior or num == superior:
        igual_limite = True

    if inferior < num < superior:
        suma_dentro += num
    else:
        fuera += 1


print("Suma de números ", suma_dentro)
print("Cantidad de números fuera ", fuera)

if igual_limite:
    print("metiste algún número igual a los límites.")
else:
    print("no metiste ningún número igual a los límites.")
