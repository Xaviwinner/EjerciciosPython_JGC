nota_10 = False  

while True:
    nota = float(input("mete una nota: "))

    if nota == -1:
        break 
    if nota == 10:
        nota_10 = True
if nota_10:
    print("Sí hubo al menos una nota con valor 10.")
else:
    print("No hubo ninguna nota con valor 10.")
