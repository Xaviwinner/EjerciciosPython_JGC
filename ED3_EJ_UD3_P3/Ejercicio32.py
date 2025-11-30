minutos = int(input("Duración : "))
dia_semana = input("Es domingo si o no, responde con s o n: ").lower()
turno = ""

if dia_semana != "s":
    turno = input("Turno m  mañana o t tarde): ").lower()

costo = 0

if minutos <= 5:
    costo = 1
elif minutos <= 8:  
    costo = 1 + (minutos - 5) * 0.80
elif minutos <= 10:  
    costo = 1 + 3 * 0.80 + (minutos - 8) * 0.70
else:  
    costo = 1 + 3 * 0.80 + 2 * 0.70 + (minutos - 10) * 0.50

if dia_semana == "s":
    impuesto = costo * 0.03
else:
    if turno == "m":
        impuesto = costo * 0.15
    else:
        impuesto = costo * 0.10

total = costo + impuesto

print("Costo : ", costo)
print("Impuesto:   ", impuesto)
print("Total a pagar:", total)
