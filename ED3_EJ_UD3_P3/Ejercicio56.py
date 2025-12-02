def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


N = int(input("numeros primos que quieres enseñar: "))

contador = 0     
numero = 2       

print(f"Los {N} primeros son:")

while contador < N:
    if es_primo(numero):
        print(numero)
        contador += 1
    numero += 1
