correctas = int(input("respuestas correctas: "))
incorrectas = int(input("respuestas incorrectas: "))
blanco = int(input("respuestas en blanco: "))

nota_final = correctas * 5 + incorrectas * (-1) + blanco * 0

print(" nota final :", nota_final)
