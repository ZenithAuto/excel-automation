palabras = input().split()
contador = 0

for p in palabras:
    if len(p) > 3:
        contador += 1

print(contador)