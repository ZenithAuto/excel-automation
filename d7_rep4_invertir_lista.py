n = int(input())
numeros = list(map(int, input().split()))

invertida = numeros[::-1]

print(" ".join(map(str, invertida)))