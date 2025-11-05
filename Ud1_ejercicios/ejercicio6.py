precio_original = float(input("precio original del artículo: "))
precio_venta = float(input("precio de venta real: "))

descuento = precio_original - precio_venta

porcentaje_descuento = (descuento / precio_original) * 100

print("El descuento es ", porcentaje_descuento, "%")