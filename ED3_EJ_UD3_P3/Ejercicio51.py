pago = 10
total = 0

for mes in range(20):
    print("Mes", mes+1, ":", pago )
    total += pago
    pago *= 2

print("Total pagado:", total,)
