def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = int(input("Ingresa un número para calcular su factorial: "))
if numero < 0:
    print("No se puede calcular el factorial de números negativos.")
else:
    resultado_factorial = factorial(numero)
    print(f"El factorial de {numero} es: {resultado_factorial}")
