cadena=input("escribe texto: ")
contador=0
for i in range(len(cadena)):
    if(cadena[i]=="a"):
        contador+=1
    else:
        contador+=0
if (contador>1):
    print("existe ese caracter")
else:
    print("no existe ese caracter")