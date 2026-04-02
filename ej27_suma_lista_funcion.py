def suma_lista(lista):
    return sum(lista)

numeros = list(map(int, input().split()))
print(suma_lista(numeros))