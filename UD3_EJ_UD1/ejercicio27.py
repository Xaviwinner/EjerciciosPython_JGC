dieces = False  

while True:
    nota = float(input("mete una nota: "))

    if nota == -1:
        break 
    if nota == 10:
        dieces = True
if dieces:
    print("Sí hubo dieces")
else:
    print("No hubo ninguna dieces")
