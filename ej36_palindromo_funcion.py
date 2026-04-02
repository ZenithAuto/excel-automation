def es_palindromo(s):
    s = s.lower()
    return s == s[::-1]

palabra = input()
print("SI" if es_palindromo(palabra) else "NO")