cadena = input("mete una letra: ")

if len(cadena) == 1 and cadena.isupper() and cadena.isalpha():
    print("Es  mayúscula.")
else:
    print("no es mayúscula.")
