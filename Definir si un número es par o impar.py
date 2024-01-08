def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "El número es par."
    else:
        return "El número es impar."

num = int(input("Ingresa un número para verificar si es par o impar: "))
resultado = es_par_o_impar(num)
print(resultado)

