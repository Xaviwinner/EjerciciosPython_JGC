asterisco="*"
espacio=" "
numero=int(input("escribe un numero"))
print(asterisco*numero)
for i in range(1,numero):
    if(i%2==0):
        print(asterisco+espacio*(numero-1)+asterisco)
    else:
        print((asterisco+espacio)*(numero//2+1))
print(asterisco*numero)
