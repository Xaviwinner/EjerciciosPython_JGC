asteriscos="*"
espacios=" "
numero=int(input("escribe un numero"))
print(asteriscos+(espacios*(numero))+asteriscos)
for i in range(1,numero//2+1):
    if(i==numero//2):
        print(asteriscos+espacios*(numero//2)+asteriscos+espacios*(numero//2)+asteriscos)
    else:
        print((asteriscos+(espacios*i)+asteriscos)+(espacios*(numero - 2 - 2*i)+asteriscos)+espacios*i+asteriscos)

for j in range (1,numero//2+1):
    print(asteriscos+espacios*numero+asteriscos)
