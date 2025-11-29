base = float(input("sueldo base: "))

venta1 = float(input("primera venta: "))
venta2 = float(input("segunda venta: "))
venta3 = float(input("tercera venta: "))

comision = (venta1 + venta2 + venta3) * 0.10
mes = base + comision

print("total del mes:", comision)
print("Total en el mes:", mes)
