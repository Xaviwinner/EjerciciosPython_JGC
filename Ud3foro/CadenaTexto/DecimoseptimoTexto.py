texto = input("Escribe una cadena: ")

nueva = ""

for c in texto:
    contador = 0
    for x in texto:
        if x == c:
            contador += 1

    if contador > 1 and c not in nueva:
        nueva += c

print("Caracteres repetidos:", nueva)
