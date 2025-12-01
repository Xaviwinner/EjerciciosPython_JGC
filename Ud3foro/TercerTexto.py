palabras=input("escribe palabras:")
contador=0
for i in range(len(palabras)):
    if(palabras[i]=="a"):
        contador+=1
    else:
        contador+=0
print(contador)