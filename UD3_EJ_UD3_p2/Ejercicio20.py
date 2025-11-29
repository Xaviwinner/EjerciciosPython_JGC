cantidad = int(input("mete tu dinero: "))

billetes = [500, 200, 100, 50, 20, 10, 5]

for b in billetes:
    num = cantidad // b
    if num > 0:
        print(num, "billetes de", b, "€")
    cantidad = cantidad % b
