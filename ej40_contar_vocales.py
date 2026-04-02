texto = input().lower()
vocales = 0

for c in texto:
    if c in "aeiou":
        vocales += 1

print(vocales)