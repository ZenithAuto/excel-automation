def es_palindromo(texto):
    texto = texto.lower()
    return texto == texto[::-1]

texto = input()
print("SI" if es_palindromo(texto) else "NO")