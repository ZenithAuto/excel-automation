def contar_letra(texto, letra):
    return texto.count(letra)

texto = input()
letra = input()
print(contar_letra(texto, letra))