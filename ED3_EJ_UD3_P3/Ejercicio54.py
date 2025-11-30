
horas = 0
minutos = 0
segundos = 0

while True:
    print(horas, ":", minutos, ":", segundos)

    segundos += 1

    if segundos == 60:
        segundos = 0
        minutos += 1

    if minutos == 60:
        minutos = 0
        horas += 1
