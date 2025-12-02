HH = int(input("Hora de salida (0-23): "))
MM = int(input("Minutos de salida (0-59): "))
SS = int(input("Segundos de salida (0-59): "))

T = int(input("Tiempo de viaje en segundos: "))

SS += T

MM += SS // 60
SS = SS % 60

HH += MM // 60
MM = MM % 60

HH = HH % 24

print(f"Hora de llegada: {HH:02d}:{MM:02d}:{SS:02d}")
