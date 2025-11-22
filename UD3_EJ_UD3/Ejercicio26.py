# Programa para evaluar puntaje de tres dados

dado1 = int(input("primer dado: "))
dado2 = int(input("segundo dado: "))
dado3 = int(input("tercer dado: "))

# Contar cuántos dados valen 6
seis = 0

if dado1 == 6:
    seis += 1
if dado2 == 6:
    seis += 1
if dado3 == 6:
    seis += 1

# Switch (match)
match seis:
    case 3:
        resultado = "Excelente"
    case 2:
        resultado = "Muy bien"
    case 1:
        resultado = "Regular"
    case 0:
        resultado = "Pésimo"

print(resultado)