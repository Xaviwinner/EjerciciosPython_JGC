
usuario_correcto = "admin"
contrasena_correcta = "1234"

usuario = input("Introduce nombre de usuario: ")
contrasena = input("Introduce contraseña: ")

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("Inicio de sesión correcto.")
elif usuario != usuario_correcto:
    print("Nombre de usuario incorrecto.")
