from datetime import datetime

# Obtener la fecha actual
fecha_actual = datetime.now()

# Definir las fechas de Día de Muertos y Navidad
dia_de_muertos = datetime(fecha_actual.year, 11, 2)
navidad = datetime(fecha_actual.year, 12, 25)

# Calcular los días que faltan para cada fecha
dias_para_dia_de_muertos = (dia_de_muertos - fecha_actual).days
dias_para_navidad = (navidad - fecha_actual).days

# Mostrar los días que faltan
print(f"Faltan {dias_para_dia_de_muertos} días para el Día de Muertos.")
print(f"Faltan {dias_para_navidad} días para Navidad.")

