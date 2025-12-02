hubo_diez = False  

while True:
    nota = float(input("Mete una nota: "))

    if nota == -1:
        break 

    if nota == 10:
        hubo_diez = True

if hubo_diez:
    print("Sí hubo dieces")
else:
    print("No hubo ningún diez")
