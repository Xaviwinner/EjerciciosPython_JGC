numero = int(input("mete un número: "))

decenas = numero // 10
unidades = numero % 10

invertido = unidades * 10 + decenas

print("Número invertido:", invertido)
