asterisco="*"
espacio=" "
cont=0
numero=int(input("escribe un numero"))
print(asterisco*numero)
for i in range(1,numero//2):
    print((asterisco)+(espacio*i+asterisco)+espacio*((numero//2)-cont)+asterisco)
    cont=cont+1  
print(asterisco+espacio*(numero//2)+asterisco+espacio+asterisco)
for j in range(1,numero//2):
    print((asterisco)+(espacio*((numero//2)-j)+asterisco)+espacio+espacio*j+asterisco)


print(asterisco*numero)