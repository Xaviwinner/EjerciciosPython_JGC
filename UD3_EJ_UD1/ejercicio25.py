nota = float(input("Mete tu nota: "))

if 0 <= nota < 3:
    print("Muy Deficiente")
elif 3 <= nota < 5:
    print("Insuficiente")
elif 5 <= nota < 6:
    print("Suficiente")
elif 6 <= nota < 7:
    print("Bien")
elif 7 <= nota < 9:
    print("Notable")
else:  # 9 a 10
    print("Sobresaliente")
