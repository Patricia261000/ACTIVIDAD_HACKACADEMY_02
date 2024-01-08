def es_palindromo(texto):
    # Convertir el texto a minúsculas y eliminar espacios y signos de puntuación
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "")

    # Verificar si el texto es igual al revés
    return texto == texto[::-1]

# Pedir al usuario que ingrese una palabra o frase
entrada = input("Ingresa una palabra o frase para verificar si es un palíndromo: ")

# Verificar si la entrada es un palíndromo
if es_palindromo(entrada):
    print(f"'{entrada}' es un palíndromo.")
else:
    print(f"'{entrada}' no es un palíndromo.")
