numero = int(input("mete el resultado: "))

if numero < 1 or numero > 6:
    print("ERROR")
else:
    opuesto = 7 - numero
    
    letras = ["uno", "dos", "tres", "cuatro", "cinco", "seis"]
    
    print("La cara opuesta es:", letras[opuesto - 1])
