nombre = input("nombre alumno: ")
facultad = input("facultad: ").lower()

match facultad:
    case "ingeniería de sistemas":
        matricula = 350
        mensual = 650
    case "derecho":
        matricula = 300
        mensual = 550
    case "ingeniería naviera":
        matricula = 300
        mensual = 500
    case "ingeniería pesquera":
        matricula = 310
        mensual = 460
    case "contabilidad":
        matricula = 280
        mensual = 490
    case "administracion":
        matricula = 360
        mensual = 520


subtotal = matricula + mensual
igv = subtotal * 0.18
total_pagar = subtotal + igv

print("alumno:", nombre)
print("facultad:", facultad)
print("Importe:", matricula)
print("cobro mensual:", mensual)
print("IGV:", igv)
print("pagar:", total_pagar)
