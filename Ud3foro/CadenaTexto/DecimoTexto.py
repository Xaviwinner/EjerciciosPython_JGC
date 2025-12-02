cadena=input("escribe letras: ")
contador=0
for i in range(len(cadena)):
    if(cadena[i].isupper()):
        contador+=1
print(contador)