A = int(input("mete el valor de A: "))
B = int(input("mete el valor de B: "))

elevado = 1

for i in range(B):
    elevado *= A

print("El resultado da:", elevado)
