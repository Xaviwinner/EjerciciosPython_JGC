punto = "."
asterisco = "*"
n = int(input("Mete un numero "))
print(punto*n)

for i in range(0,n//2):
    print(punto * i +asterisco +punto * (n//2 - i - 1) +asterisco +punto * (n//2 - i - 1) +asterisco+punto*i)

print(asterisco * n)

for i in range(n//2 - 1, -1, -1):
    print(punto * i +asterisco +punto * (n//2 - i - 1) +asterisco +punto * (n//2 - i - 1) +asterisco+punto*i)
      
print(punto*n)
