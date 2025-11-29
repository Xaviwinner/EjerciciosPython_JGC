asterisco="*"
espacio=" "
numero=int(input("escribe un numero:"))
for i in range(1,numero):
    print((espacio*i+asterisco*(numero-i))+asterisco+(asterisco*(numero-i)))
print(espacio*numero+asterisco)