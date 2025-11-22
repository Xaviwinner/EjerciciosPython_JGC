espacio = " "
asteriscos = "*"


numero = int(input("Introduce un numero: "))
print(espacio*(numero-1),asteriscos)
for i in range(1,numero):
    print(espacio*(numero-i)+asteriscos*(i)+asteriscos*(i))

for k in range(numero,0,-1):
    print(espacio*(numero-k)+asteriscos*(k)+asteriscos*(k))

print(espacio*(numero),asteriscos)
