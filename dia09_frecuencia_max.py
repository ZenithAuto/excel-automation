from collections import Counter

palabras = input().split()
conteo = Counter(palabras)

max_frec = max(conteo.values())

resultado = []
for palabra, freq in conteo.items():
    if freq == max_frec:
        resultado.append(palabra)

resultado.sort()

for p in resultado:
    print(p)