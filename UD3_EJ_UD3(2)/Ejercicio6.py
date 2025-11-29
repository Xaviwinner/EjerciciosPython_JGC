numero = int(input("Mete el valor:"))

factorial = 1
for i in range(1, numero + 1):
    factorial = i * factorial
print(factorial)   