horasT = 0
for dia in range(1, 7):
    horas = float(input(f"mete las horas trabajadas {dia}: "))
    horasT += horas

pago = float(input("mete el pago por hora: "))

sueldo = horasT * pago

print("Total de horas", horasT)
print("Sueldo:", sueldo)
