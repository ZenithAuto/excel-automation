palabra = input().lower()

vocales = "aeiou"
# Filtramos solo letras para no contar números o espacios como consonantes
solo_letras = [c for c in palabra if c.isalpha()]

cant_vocales = sum(1 for c in solo_letras if c in vocales)
cant_consonantes = len(solo_letras) - cant_vocales

# Un palíndromo es igual al derecho y al revés
es_palindromo = "SI" if palabra == palabra[::-1] else "NO"

print(cant_vocales)
print(cant_consonantes)
print(es_palindromo)