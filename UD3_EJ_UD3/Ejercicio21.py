nombre = input("Trabajador: ")
horas = float(input("Horas trabajadas: "))
salario = float(input("Tarifa: "))

if horas <= 35:
    bruto = horas * salario
else:
    extras = horas - 35
    bruto = (35 * salario) + (extras * salario * 1.5)

impuestos = 0

if bruto > 500:
    exceso = bruto - 500
else:
    exceso = 0

if exceso > 400:
    impuestos += 400 * 0.25
    exceso -= 400
else:
    impuestos += exceso * 0.25
    exceso = 0

if exceso > 0:
    impuestos += exceso * 0.45

neto = bruto - impuestos

print(f"Salario bruto: {bruto:.2f} €")
print(f"Impuestos: {impuestos:.2f} €")
print(f"Salario neto: {neto:.2f} €")
