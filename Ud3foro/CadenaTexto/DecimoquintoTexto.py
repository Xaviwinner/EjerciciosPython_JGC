texto = input("Escribe un texto: ")
nuevo = ""

vocales = "aeiouAEIOU"

for c in texto:
    if c in vocales:
        nuevo += "*"
    else:
        nuevo += c

print("Nueva cadena:", nuevo)
