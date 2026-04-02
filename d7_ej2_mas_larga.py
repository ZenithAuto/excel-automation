frase = input()
palabras = frase.split()

if palabras:
    # max() con key=len devuelve la palabra con más caracteres.
    # En caso de empate, Python devuelve la primera encontrada por defecto.
    mas_larga = max(palabras, key=len)
    print(mas_larga)