palabras = input().split()
largas = []

for p in palabras:
    if len(p) > 4:
        largas.append(p)

print(largas)