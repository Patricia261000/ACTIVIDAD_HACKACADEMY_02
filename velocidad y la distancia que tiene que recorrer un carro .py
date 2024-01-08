# Solicitar al usuario la velocidad y la distancia
velocidad = float(input("Ingresa la velocidad del carro (en km/h): "))
distancia = float(input("Ingresa la distancia a recorrer (en kilómetros): "))

# Calcular el tiempo requerido
tiempo = distancia / velocidad

# Mostrar el resultado
print(f"El tiempo requerido para recorrer {distancia} kilómetros a {velocidad} km/h es: {tiempo} horas")
