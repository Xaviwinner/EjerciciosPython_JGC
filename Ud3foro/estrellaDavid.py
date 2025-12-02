asterisco="*"
espacio=" "
numero=int(input("ESCRIBE UN NUMERO:"))
print(numero*(espacio*5)+asterisco)
for i in range(1,numero):
    print((espacio*((numero*5)-i)+asterisco)+((espacio*((i*2)-1))+asterisco))

print(espacio*(numero*2)+asterisco*((numero*2))+asterisco*((numero*2))+asterisco*((numero*2)+1))

for i in range(1,numero):
    print(espacio*((numero*2))+espacio*(i)+asterisco+(espacio*((numero-i)-1))+espacio*((numero-i)-1)+espacio+(asterisco+(espacio*(numero*2)+espacio*((i*2)-1)+asterisco))+(espacio*((numero-i)-1))+espacio+espacio*((numero-i)-1)+asterisco)
print((numero*(espacio*3)+asterisco)+((((numero*4)-1)*((espacio)))+asterisco))


for i in range(0,numero):
    print(espacio*((numero*2))+espacio*(numero-i)+asterisco+espacio*i+((espacio*i))+asterisco+(espacio*((numero*2)-2))+espacio*(numero-i)+espacio*(numero-i)+asterisco+espacio*i+espacio*i+asterisco)

print(espacio*(numero*2)+asterisco*((numero*2))+asterisco*((numero*2))+asterisco*((numero*2)+2))

for i in range(1,numero):
    print(espacio*(numero*4)+espacio*i+asterisco+espacio*(numero-i)+espacio*((numero-i)-1)+asterisco)

print(numero*(espacio*5)+asterisco)

