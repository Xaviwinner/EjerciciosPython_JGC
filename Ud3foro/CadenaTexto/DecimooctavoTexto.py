texto = input("Escribe una cadena: ")
consonantes = ""

vocales = "aeiouAEIOU"

for c in texto:
    if ("a" <= c <= "z" or "A" <= c <= "Z") and c not in vocales:
        consonantes += c

print("Consonantes:", consonantes)
