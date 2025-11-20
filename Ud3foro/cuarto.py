numero = int(input("mete un numero: "))

asterisco = "*"
espacio = " "

for bloques in range(numero):          
    for filas in range(3):  
        linea = ""
        for columnas in range(numero):   
            if (bloques + columnas) % 2 == 0:
                linea += asterisco * 3
            else: 
                linea += espacio * 3
            linea += espacio
        print(linea)
