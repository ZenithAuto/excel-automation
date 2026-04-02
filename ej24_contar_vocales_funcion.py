def contar_vocales(texto):
    texto = texto.lower()
    contador = 0
    for letra in texto:
        if letra in "aeiou":
            contador += 1
    return contador

texto = input()
print(contar_vocales(texto))