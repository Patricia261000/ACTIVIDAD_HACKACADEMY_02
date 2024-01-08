def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

# Pedir al usuario que ingrese un año
anio = int(input("Ingresa un año para verificar si es bisiesto: "))

# Verificar si el año es bisiesto
if es_bisiesto(anio):
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")
