from datetime import datetime

# Pedir al usuario su fecha de nacimiento en el formato 'YYYY-MM-DD'
fecha_nacimiento_str = input("Ingresa tu fecha de nacimiento (YYYY-MM-DD): ")

# Convertir la cadena de texto a un objeto datetime
fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d")

# Obtener la fecha actual
fecha_actual = datetime.now()

# Calcular la diferencia entre las fechas
diferencia = fecha_actual - fecha_nacimiento

# Calcular los años bisiestos entre las fechas
bisiestos = 0
for year in range(fecha_nacimiento.year, fecha_actual.year + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        bisiestos += 1

# Calcular los días vividos considerando años bisiestos
total_dias_vividos = diferencia.days + bisiestos

# Mostrar el número de días vividos
print(f"Has vivido {total_dias_vividos} días contando años bisiestos.")
