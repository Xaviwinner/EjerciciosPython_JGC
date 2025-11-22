
horas = int(input("METE las horas : "))
minutos = int(input("METE los minutos : "))
segundos = int(input("METE los segundos : "))

segundos += 1

if segundos == 60:
    segundos = 0
    minutos += 1
    if minutos == 60:
        minutos = 0
        horas += 1
        if horas == 24:
            horas = 0

print("Dentro de un segundo serán las:", horas, minutos, segundos)
