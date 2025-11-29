pares = 0
impares = 0

for n in range(100, 201):  
    if n % 2 == 0:
        pares += n
    else:
        impares += n

print("  pares:", pares)
print("  impares:", impares)
