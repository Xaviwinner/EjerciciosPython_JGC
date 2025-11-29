asterisco="*"
espacio=" "
numero=int(input("dime un numero:"))
print(espacio*(numero+1)+asterisco)
for i in range(0,numero):
    if(i==numero//2):
        if(numero%2==0):
            print(espacio*i+(asterisco+espacio)*(i+2))
        else:
            print(espacio*(i+1)+(asterisco+espacio)*(i+2))

    else:
        print(((numero-i)*espacio+asterisco)+espacio+((i*2)*espacio)+asterisco)
        
print(((numero*2)+3)*asterisco)