N = int(input("numero de trabajadores: "))

total = 0

for i in range(1, N + 1):
    horas = float(input(f"Horas trabajadas {i}: "))
    pago = float(input(f"Pago por hora {i}: "))

    sueldo = horas * pago
    print("Sueldo semanal", sueldo )

    total += sueldo

print("\nPago total de la empresa:", total)
