espacio=" "
asterisco="*"
numero=int(input("escribe un numero:"))


print((espacio*(numero+1))+asterisco)
for i in range(0,numero):
    print(((numero-i)*espacio+asterisco)+((espacio+(i*espacio)*2)+asterisco))

for k in range(1,numero+1):
    print(((k*espacio)+asterisco)+espacio+((numero-k)*2)*espacio+asterisco)
    
print((espacio*(numero+1))+asterisco)
