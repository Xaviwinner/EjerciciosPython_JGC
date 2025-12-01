asterisco="*"
espacio=" "
numero=int(input("dime un numero: "))

for i in range(0,numero):
    print((asterisco+espacio+(espacio*i)+asterisco)+espacio+(espacio*((numero*2)-(i*2))+asterisco)+espacio*(i)+espacio+asterisco)

print((asterisco+espacio*(numero+2)+asterisco+espacio*(numero+2)+asterisco))

for k in range(0,numero):
    print((asterisco+((numero-k)*espacio)+asterisco)+((espacio*k)+espacio+espacio+espacio+(espacio*k+asterisco)+espacio*(numero-k)+asterisco))