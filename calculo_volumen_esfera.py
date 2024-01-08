import math

def calcular_volumen_esfera(radio):
    volumen = (4/3) * math.pi * radio**3
    return volumen

# Ingresa el radio de la esfera
radio_esfera = float(input("Ingresa el radio de la esfera: "))

# Calcula el volumen llamando a la función
volumen_esfera = calcular_volumen_esfera(radio_esfera)

# Imprime el resultado
print(f"El volumen de la esfera con radio {radio_esfera} es: {volumen_esfera}")
