valor_compra = float(input("cuanto ha costadp "))
pago = input("contado o tarjeta ").lower()

descuento = 0
recargo = 0

if pago == "contado":
    descuento = valor_compra * 0.05
    total = valor_compra - descuento
elif pago == "tarjeta":
    recargo = valor_compra * 0.03
    total = valor_compra + recargo


print("precio de compra:", valor_compra)
print("Descuento :", descuento)
print("Recargo :", recargo)
print("precio pagado:", total)
