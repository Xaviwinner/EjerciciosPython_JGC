asterisco="*"
puntos="."
numero=int(input("escribe un numero"))
print(((numero*2)+3)*puntos)
for i in range(1,numero):
    print(((puntos*i)+asterisco)+((puntos*(numero-i))+asterisco)+(puntos*((numero-i))+asterisco)+puntos*(i))

print(asterisco*((numero*2)+3))

for j in range(1,numero):
    print((puntos*((numero-j))+asterisco)+(puntos*j+asterisco)+(puntos*j+asterisco)+puntos*(numero-j))
print(((numero*2)+3)*puntos)
