p1 = float(input("nota del parcial 1: "))
p2 = float(input("nota del parcial 2: "))
p3 = float(input("nota del parcial 3: "))

examen = float(input("nota del examen final: "))
trabajo = float(input("nota del trabajo final: "))
media = (p1 + p2 + p3) / 3

nota = (media * 0.55) + (examen * 0.30) + (trabajo * 0.15)

print("La nota final es:", nota)
