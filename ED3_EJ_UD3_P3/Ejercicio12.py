import math

x1 = float(input("mete x1: "))
y1 = float(input("mete y1: "))

x2 = float(input("mete x2: "))
y2 = float(input("mete y2: "))
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(" distancia entre puntos:", distancia)