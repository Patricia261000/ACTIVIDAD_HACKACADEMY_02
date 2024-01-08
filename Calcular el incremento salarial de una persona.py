salario_actual = float(input("Ingresa tu salario actual: "))

if salario_actual < 15000:
    incremento = salario_actual * 0.20  # 20% de incremento
else:
    incremento = salario_actual * 0.15  # 15% de incremento

salario_incrementado = salario_actual + incremento

print(f"Tu salario incrementado es: {salario_incrementado}")
