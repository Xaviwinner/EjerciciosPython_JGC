def invertir_cadena(cadena):
    indice = len(cadena) - 1
    cadena_invertida = ''
    while indice >= 0:
        cadena_invertida += cadena[indice]
        indice -= 1
    return cadena_invertida   