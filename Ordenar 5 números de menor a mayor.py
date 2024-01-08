# Pedir al usuario que ingrese 5 números
numeros = []
for i in range(5):
    num = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)

# Ordenar los números de menor a mayor
numeros.sort()

# Mostrar los números ordenados
print("Números ordenados de menor a mayor:")
for num in numeros:
    print(num)
