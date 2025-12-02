cadena=input("escribe una cadena de texto: ")
vacio = " "
cadena_nueva = ""
for i in cadena:
    if (i in cadena):
        if i in vacio:
            cadena_nueva += i + i
        else:
            cadena_nueva += i
print(cadena)  