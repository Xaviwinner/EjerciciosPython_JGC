nombre = input("Nombre : ")
horas = float(input("Horas trabajadas: "))
tarifa = float(input("Tarifa por hora: "))

if horas <= 35:
    salario_bruto = horas * tarifa
else:
    horas_normales = 35
    horas_extra = horas - 35
    salario_bruto = (horas_normales * tarifa) + (horas_extra * tarifa * 1.5)

impuesto = 0
restante = salario_bruto

if restante > 500:
    restante -= 500
else:
    restante = 0

if restante > 0:
    if restante <= 400:
        impuesto += restante * 0.25
        restante = 0
    else:
        impuesto += 400 * 0.25
        restante -= 400

if restante > 0:
    impuesto += restante * 0.45

salario_neto = salario_bruto - impuesto

print("Salario bruto", salario_bruto, 2)
print("Impuestos totales", impuesto, 2)
print("Salario neto", salario_neto, 2)
