asterisco="*"
espacio=" "
numero=int(input("escribe un numero: "))
print((espacio*(numero*5))+asterisco)
for i in range(1,numero):
    print((espacio*((numero*5)-i)+asterisco)+((espacio*((i*2)-1))+asterisco))
print((espacio*(numero*4))+(asterisco+espacio)*((numero+1)))




print(((espacio*((numero*4)-1))+asterisco)+espacio*((numero*2)+1)+asterisco)


for i in range(1,numero):
    print((espacio*(((numero*4)-i)-1)+asterisco)+((espacio*((i*2)-1))+asterisco)+espacio+(espacio*(numero-i))+(espacio*(numero-i)+asterisco)+((espacio*((i*2)-1))+asterisco))
print((espacio*((numero*3)-1))+(asterisco+espacio)*((numero*2)+2))




print(((espacio*((numero*3)-2))+asterisco)+espacio*((numero*4)+3)+asterisco)
for i in range(1,numero):
    print((espacio*(((numero*3)-i)-2)+asterisco)+((espacio*((i*2)-1))+asterisco)+espacio*(numero-i)+espacio*(numero-i)+espacio*(i)+espacio*(numero-i)+espacio*(i)+espacio*((numero-i)+3)+asterisco+espacio*((i*2)-1)+asterisco)
print((espacio*((numero*2)-2))+(asterisco+espacio)*((numero+1))+(espacio*((numero*2)+2))+(asterisco+espacio)*((numero+1)))


print(((espacio*((numero*2)-3))+asterisco)+espacio*((numero*2)+1)+asterisco+espacio*((numero*2)+1)+asterisco+espacio*((numero*2)+1)+asterisco)


for i in range(1,numero):
    print((espacio*(((numero*2)-i)-3)+asterisco)+((espacio*((i*2)-1))+asterisco)+espacio+(espacio*(numero-i))+(espacio*(numero-i)+asterisco)+((espacio*((i*2)-1))+asterisco)+espacio+(espacio*(numero-i))+espacio*(numero-i)+asterisco+((espacio*((i*2)-1))+asterisco)+espacio+(espacio*(numero-i))+(espacio*(numero-i)+asterisco)+(((i*2)-1)*espacio)+asterisco)
print((espacio*((numero)-3))+(asterisco+espacio)*((numero*4)+4))