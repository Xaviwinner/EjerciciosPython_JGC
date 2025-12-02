numero = int(input("Introduce número entre 0 y 99999: "))

if 0 <= numero <= 99999:
    cifras = len(str(numero))
    print("El número tiene", cifras, "cifras.")
