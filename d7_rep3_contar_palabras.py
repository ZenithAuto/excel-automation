texto = input().lower()
palabras = texto.split()

frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

for palabra in sorted(frecuencia):
    print(palabra, frecuencia[palabra])