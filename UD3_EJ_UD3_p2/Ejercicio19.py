print("piensa un numero")

minimo = 1
maximo = 100

while True:
    intento = (minimo + maximo) // 2
    print("¿Es", intento, "?")
    respuesta = input("(Responde si es mayor menor o igual): ")

    if respuesta == "mayor":
        minimo = intento + 1
    elif respuesta == "menor":
        maximo = intento - 1
    elif respuesta == "igual":
        print("tu numero es", intento)
        break
