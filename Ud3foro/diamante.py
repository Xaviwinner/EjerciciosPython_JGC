espacio = " "
asteriscos = "*"


numero = int(input("Introduce un numero: "))
print(espacio*(numero-1),asteriscos)

for j in range(1,numero):
    print(espacio*(numero-j)+asteriscos+espacio*(j-1)+espacio*(j-1),asteriscos)
for k in range(numero,0,-1):
    print(espacio*(numero-k)+asteriscos+espacio*(k-1)+espacio*(k-1),asteriscos)

print(espacio*(numero-1),asteriscos)
