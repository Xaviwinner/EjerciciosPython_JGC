cantidad = int(input("Introduce una cantidad : "))

billetes = [500, 200, 100, 50, 20, 10, 5]


for b in billetes:
    if cantidad >= b:
        num_billetes = cantidad // b
        cantidad -= num_billetes * b
        print(f"{num_billetes} billetes de {b} €")
