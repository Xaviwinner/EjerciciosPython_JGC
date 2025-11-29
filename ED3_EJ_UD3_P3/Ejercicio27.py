nota = float(input("mete la nota: "))
edad = int(input("mete la edad: "))
sexo = input("mete el sexo (M/F): ")

if nota >= 5 and edad >= 18 and sexo == "F":
    print("ACEPTADA")
elif nota >= 5 and edad >= 18 and sexo == "M":
    print("POSIBLE")
else:
    print("NO ACEPTADA")
