espacio = " "
asterisco = "*"
n = int(input("Mete un numero "))

for i in range(0,n//2):
    print(espacio * i +asterisco +espacio * (n//2 - i - 1) +asterisco +espacio * (n//2 - i - 1) +asterisco)

print(asterisco * n)

for i in range(n//2 - 1, -1, -1):
    print(espacio * i +asterisco +espacio * (n//2 - i - 1) +asterisco +espacio * (n//2 - i - 1) +asterisco)
