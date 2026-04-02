texto = input()
palabras = texto.split()

for i in range(len(palabras)):
    palabras[i] = palabras[i].capitalize()

print(" ".join(palabras))