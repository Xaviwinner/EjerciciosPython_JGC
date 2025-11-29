positivos = 0
negativos = 0


while True:
    num = int(input("mete numero:"))

    if num == 0:
        break  

    if num > 0:
        positivos += 1
    else:
        negativos += 1

print("Positivos: "+str(positivos))
print("Negativos: "+str(negativos))

