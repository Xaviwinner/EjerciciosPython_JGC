puntos="."
asteriscos="*"
espacios=" "
numero=int(input("escribe un numero"))

print((puntos+espacios)*numero)
for i in range(1,numero//2):
  
        print((puntos+espacios)+(asteriscos+espacios+puntos+espacios)*(i))
        
print((asteriscos+espacios)*numero)
      
    