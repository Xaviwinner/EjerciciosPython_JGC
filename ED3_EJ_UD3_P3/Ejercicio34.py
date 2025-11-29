dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

def bisiesto(a):
    return (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)

if mes < 1 or mes > 12:
    print("Fecha incorrecta.")
else:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        maximo = 31
    elif mes in [4, 6, 9, 11]:
        maximo = 30
    else:  
        maximo = 29 if bisiesto(año) else 28
    if 1 <= dia <= maximo:
        print(" fecha correcta.")
    else:
        print("Fecha incorrecta.")
