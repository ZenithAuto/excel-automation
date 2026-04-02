palabras = input().split()
conteo = {}

for p in palabras:
    if p in conteo:
        conteo[p] += 1
    else:
        conteo[p] = 1

mas = max(conteo, key=conteo.get)
print(mas)