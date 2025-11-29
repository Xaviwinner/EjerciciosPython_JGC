d = float(input("mete  distancia entre los vehículo: "))
v1 = float(input("mete  velocidad del vehículo delantero: "))
v2 = float(input("mete  velocidad del vehículo que va detrás: "))

diferencia = v2 - v1

if diferencia <= 0:
    print(" vehículo de atrás no alcanzará al otro.")
else:
    tiempo_horas = d / diferencia
    tiempo_minutos = tiempo_horas * 60

    print(" vehículo alcanzará al otro en", tiempo_minutos)
