num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

if num1 == num2 == num3:
    print("Los tres números son iguales.")

else:
    mayor = num1
    menor = num1

    if num2 > mayor:
        mayor = num2
    if num3 > mayor:
        mayor = num3

    if num2 < menor:
        menor = num2
    if num3 < menor:
        menor = num3

    print("El número mayor es:", mayor)
    print("El número menor es:", menor)

