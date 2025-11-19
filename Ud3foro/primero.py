espacio = " "
asteriscos = "*"


numero = int(input("Introduce un numero: "))
print(espacio*(numero),asteriscos)
for i in range(1,numero):
    print(espacio*(numero-i)+asteriscos+espacio*(i-1),asteriscos)

for k in range(numero,0,-1):
    print(espacio*(numero-k)+asteriscos+espacio*(k-1),asteriscos)
print(espacio*(numero),asteriscos)



#primera vuelta i=0 numero-0 = 5
# seguda i=1 n-1=4
















