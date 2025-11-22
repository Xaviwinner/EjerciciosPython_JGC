NOta = float(input("mete la nota: "))

match NOta:
    case A if 0 <= A < 3:
        print("Muy Deficiente")
    case B if 3 <= B < 5:
        print("Insuficiente")
    case C if 5 <= C < 6:
        print("Suficiente")
    case D if 6 <= D < 7:
        print("Bien")
    case E if 7 <= E < 9:
        print("Notable")
    case F if 9 <= F <= 10:
        print("Sobresaliente")

