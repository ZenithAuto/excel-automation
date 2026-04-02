def contar_vocales(texto):
    contador = 0
    for c in texto.lower():
        if c in "aeiou":
            contador += 1
    return contador

texto = input()
print(contar_vocales(texto))