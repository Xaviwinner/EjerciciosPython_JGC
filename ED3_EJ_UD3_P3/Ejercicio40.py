suma = 0
contador = 0

while True:
    num = float(input("mete un numero: "))

    if num == 0:
        break
    
    suma += num
    contador += 1

if contador > 0:
    media = suma / contador
else:
    media = 0

print("Suma total:", suma)
print("Media:", media)
