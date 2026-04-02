lista1 = list(map(int, input().split()))
lista2 = list(map(int, input().split()))

resultado = []
for a, b in zip(lista1, lista2):
    resultado.append(a + b)

print(resultado)