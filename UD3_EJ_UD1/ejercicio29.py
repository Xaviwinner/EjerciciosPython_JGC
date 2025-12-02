print("Piensa un número ")
print("responde: mayor / menor / igual")

minimo = 1
maximo = 100

while True:
    intento = (minimo + maximo) // 2  
    print(f"¿Es {intento}?")
    
    respuesta = input("Respuesta (mayor / menor / igual): ").lower()

    if respuesta == "igual":
        print("lo adivine")
        break

    elif respuesta == "mayor":
        minimo = intento + 1   

    elif respuesta == "menor":
        maximo = intento - 1   

    else:
        print("Respuesta no válida. ")
