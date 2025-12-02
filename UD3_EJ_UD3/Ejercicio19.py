saldo = 10000

print("1. Introducir dinero")
print("2. Sacar dinero")
print("3. Salir")

opcion = int(input("Elige una opción: "))

if opcion == 1:
    introducir = float(input("Cantidad a ingresar: "))
    saldo += introducir
    print("Cantidad final:", saldo)

elif opcion == 2:
    sacar = float(input("Cantidad a sacar: "))
    if sacar > saldo:
        print("No tienes suficiente dinero.")
    else:
        saldo -= sacar
        print("Cantidad final:", saldo)

elif opcion == 3:
    print("Has salido del programa.")

else:
    print("Opción no válida.")
