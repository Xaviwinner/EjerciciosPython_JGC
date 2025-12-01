asterisco="*"
espacio=" "
numero=int(input("escribe un numero"))

for i in range(1,numero):
    print(((espacio*i)+asterisco)+((espacio*(numero-i))+asterisco)+(espacio*((numero-i))+asterisco))

print(asterisco*((numero*2)+2))

for j in range(1,numero):
    print((espacio*((numero-j))+asterisco)+(espacio*j+asterisco)+(espacio*j+asterisco))