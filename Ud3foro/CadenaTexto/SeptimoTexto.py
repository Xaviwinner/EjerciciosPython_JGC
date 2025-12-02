texto = input("mete una frase: ")
reemplazar = input("reemplazar: ")
nuevo = input("Nuevo: ")

resultado = ""

for i in (texto):
    if i == reemplazar:
        resultado = resultado + nuevo  
    else:
        resultado = resultado + i      

print("Resultado:", resultado)