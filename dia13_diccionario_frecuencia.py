palabras = input().split()
frecuencia = {}

for p in palabras:
    if p in frecuencia:
        frecuencia[p] += 1
    else:
        frecuencia[p] = 1

print(frecuencia)