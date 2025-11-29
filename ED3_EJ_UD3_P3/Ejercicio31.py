alumnos = int(input("Número de alumnos: "))

if alumnos >= 100:
    precio = 65
    pago = alumnos * precio

elif 50 <= alumnos <= 99:
    precio = 70
    pago = alumnos * precio
elif 30 <= alumnos <= 49:
    precio = 95
    pago = alumnos * precio
else: 
    pago = 4000
    precio = 4000 / alumnos

print("Pago a la compañía de autobuses:", pago)
print("Pago por alumno:", precio)