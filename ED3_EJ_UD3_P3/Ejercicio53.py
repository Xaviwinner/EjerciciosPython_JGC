N = int(input("numero trabajadores empresa "))

total_empresa = 0  

for trabajador in range(1, N + 1):
    print(f" {trabajador} ---")
    
    dias = int(input("dias trabajados esta semana: "))
    pago_hora = float(input("ganado por hora "))

    horas_totales = 0
    
    for d in range(1, dias + 1):
        horas = float(input(f"  Horas trabajadas  {d}: "))
        horas_totales += horas

    sueldo = horas_totales * pago_hora
    total_empresa += sueldo

    print(f"Sueldo semanal  {trabajador}: {sueldo:.2f} ")

print(f"Total que pagará: {total_empresa:.2f}")
