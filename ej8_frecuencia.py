palabras = input().split()
frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print(max(frecuencia, key=frecuencia.get))