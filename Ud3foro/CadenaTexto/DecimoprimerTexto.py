cadena=input("escribe una cadena de texto: ")
vocales = "aeiouAEIOU"
cadena_nueva = ""
for i in range(cadena):
    if (i in cadena):
        if i in vocales:
            cadena_nueva += i + i
        else:
            cadena_nueva += i
print(cadena)  

# def duplicar_vocales(cadena):
#     vocales = "aeiouAEIOU"
#     cadena_nueva = ""
#     for letra in cadena:
#         if letra in vocales:
#             cadena_nueva += letra + letra
#         else:
#             cadena_nueva += letra
#     return cadena_nueva

# mensaje = input("escribe texto: ")
# mensaje_con_vocales_duplicadas = duplicar_vocales(mensaje)
# print(mensaje_con_vocales_duplicadas)   