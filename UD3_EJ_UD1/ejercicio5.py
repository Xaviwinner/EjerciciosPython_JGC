pi = 3.1416

radio = float(input("Introduce la longitud del radio: "))

diametro = 2 * radio

longitud_circunferencia = pi * diametro

area_circulo = pi * (radio ** 2)

volumen_esfera = (4 / 3) * pi * (radio ** 3)

print("Resultados:")
print("Longitud de la circunferencia:", longitud_circunferencia)
print("Área del círculo:", area_circulo)
print("Volumen de la esfera:", volumen_esfera)