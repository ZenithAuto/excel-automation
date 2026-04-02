texto = input()
conteo = {}

for c in texto:
    if c != " ":
        conteo[c] = conteo.get(c, 0) + 1

for k in conteo:
    print(k, conteo[k])