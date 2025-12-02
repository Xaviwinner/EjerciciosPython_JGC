texto = input("Escribe un texto: ")
sin_espacios = ""

for c in texto:
    if c != " ":          
        sin_espacios += c

print("Cadena sin espacios:", sin_espacios)
