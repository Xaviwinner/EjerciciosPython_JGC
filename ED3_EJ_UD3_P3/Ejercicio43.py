primero = int(input("mete el primer numero: "))
ultimo = int(input("mete el segundo numero: "))


if primero > ultimo:
    primero, ultimo = ultimo, primero

for num in range(primero, ultimo + 1):
    if num % 2 == 0:
        print(num)
