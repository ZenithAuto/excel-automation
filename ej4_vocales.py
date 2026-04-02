texto = input().lower()
contador = 0

for letra in texto:
    if letra in "aeiou":
        contador += 1

print(contador)