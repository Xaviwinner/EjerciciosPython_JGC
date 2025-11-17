numero = int(input("Introduce lo que quieras hacer:1. introducir dinero 2. sacar dinero 3. salir"))
nuevacantidad=0
dineromaximo=10000
if numero ==1:
    introducir = int(input("Introduce la cantidad que quieres meter"))
    nuevacantidad=dineromaximo+introducir
    print("esta es tu cantidad final:",nuevacantidad)
elif numero==2:
    sacar = int(input("Introduce la cantidad que quieres sacar"))
    nuevacantidad=dineromaximo-sacar
    print("esta es tu cantidad final:",nuevacantidad)

else:
        print("te has salido")