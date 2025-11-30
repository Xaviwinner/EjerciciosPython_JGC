while True:
    caracter = input("mete un caracter: ")

    if caracter == " ":
        print("Fin")
        break

    if caracter in ["a", "e", "i", "o", "u"]:
        print("VOCAL")
    else:
        print("NO VOCAL")
