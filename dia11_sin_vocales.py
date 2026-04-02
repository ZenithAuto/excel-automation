texto = input()
resultado = ""

for c in texto:
    if c.lower() not in "aeiou":
        resultado += c

print(resultado)