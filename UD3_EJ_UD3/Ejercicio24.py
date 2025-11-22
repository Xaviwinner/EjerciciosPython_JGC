total = float(input("mete el total: "))
dia = input("mete el dia de la semana: ").lower()

descuento = 0

if dia == "martes" or dia == "jueves":
    descuento = total * 0.15

total = total - descuento

print("total de la compra:", total)
print("Descuento:", descuento)
print("pago:", total)
