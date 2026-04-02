def contar_positivos(lista):
    contador = 0
    for n in lista:
        if n > 0:
            contador += 1
    return contador

n = int(input())
numeros = list(map(int, input().split()))
print(contar_positivos(numeros))