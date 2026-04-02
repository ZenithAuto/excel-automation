n = int(input())
numeros = list(map(int, input().split()))

frecuencia = {}

for num in numeros:
    frecuencia[num] = frecuencia.get(num, 0) + 1

ordenados = sorted(numeros, key=lambda x: (-frecuencia[x], x))

print(" ".join(map(str, ordenados)))