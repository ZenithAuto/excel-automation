palabras = input().split()
mayor = palabras[0]

for p in palabras:
    if len(p) > len(mayor):
        mayor = p

print(mayor)