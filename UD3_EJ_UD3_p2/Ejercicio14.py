asterisco="*"
espacio=" "
n=int(input("escribe un numero:"))
print(espacio*n+asterisco)
for i in range(1,n):
    print((espacio*(n-i)+asterisco*i)+asterisco+(asterisco*i))