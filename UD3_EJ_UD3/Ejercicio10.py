num1 = float(input("Introduce primer número: "))
num2 = float(input("Introduce segundo número: "))

suma = num1 + num2
resta = num1 - num2
producto = num1 * num2

print("\nLa suma es:", suma)
print("La resta es:", resta)
print("El producto es:", producto)

if num2 != 0:
    division = num1 / num2
    print("La división es:", division)
else:
    print("No se puede dividir entre cero.")