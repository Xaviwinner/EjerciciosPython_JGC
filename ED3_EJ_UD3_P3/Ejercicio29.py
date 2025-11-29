A = float(input("mete el lado A: "))
B = float(input("mete el lado B: "))
C = float(input("mete el lado C: "))

 
lados = sorted([A, B, C])
a, b, c = lados   

if abs(c**2 - (a**2 + b**2)) < 1e-9:  
    print(" triángulo rectángulo.")

elif A == B == C:
    print(" triángulo equilátero.")

elif A == B or A == C or B == C:
    print(" triángulo isósceles.")

else:
    print(" triángulo escaleno.")
