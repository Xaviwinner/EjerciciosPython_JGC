valor_compra = float(input("¿Cuánto ha costado? "))
pago = input("¿Contado o tarjeta? ").lower()

descuento = 0
recargo = 0

if pago == "contado":
    descuento = valor_compra * 0.05
    total = valor_compra - descuento

elif pago == "tarjeta":
    recargo = valor_compra * 0.03
    total = valor_compra + recargo

else:
    print("Forma de pago no válida.")
    total = valor_compra  
    exit()

print("Precio de compra:", valor_compra)
print("Descuento:", descuento)
print("Recargo:", recargo)
print("Precio pagado:", total)
