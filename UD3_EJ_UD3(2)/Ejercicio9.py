

positivos=0
negativos = 0

for i in range(100):
    numero = int(input("Mete un número: "))
if numero==0:
    print("total de negativosd", negativos)
    print("total de positivos", positivos)

else:
    if numero<0:
        negativos +=1
    else:
        positivos+=1

print("total de negativosd", negativos)
print("total de positivos", positivos)



  