import random


numero_secreto = random.randint(1, 100)
intentos = 10
contador = 0

while intentos > 0:
    num = int(input("mete un número : "))
    contador += 1
    intentos -= 1

    if num == numero_secreto:
        print(f"acertaste el numero")
        break
    elif num < numero_secreto:
        print("El número  es mayor.")
    else:
        print("El número  es menor.")

if intentos == 0 and num != numero_secreto:
    print("perdiste.")
