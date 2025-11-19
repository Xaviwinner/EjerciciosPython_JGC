negativo = False
positivo=0
negativo=0
print("Ingrese 100 números :")

for i in range(1, 101):
    numerp = float(input("Ingrese el número : "))
    if numerp == 0:
       break
    if numerp < 0:
        negativo = True
        negativo+1
    else:
        positivo+1
    print("cantidad de negativos",negativo)
    print("cantidad de positivos"+positivo)
