positivos = 0
negativos = 0


for i in range(1, 100):
    num = int(input("mete 100 números :"))
    if num > 0:
        positivos += 1
    else:
        negativos += 1

print(" positivos: "+str(positivos))
print(" negativos: "+str(negativos))
