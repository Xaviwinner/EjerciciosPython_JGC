texto = input("Escribe un texto: ")
contador = 0

for c in texto:
    if "0" <= c <= "9":   
        contador += 1

print("Cantidad de números:", contador)
