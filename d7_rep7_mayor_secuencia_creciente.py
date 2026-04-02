n = int(input())
numeros = list(map(int, input().split()))

max_len = 1
actual = 1

for i in range(1, n):
    if numeros[i] > numeros[i - 1]:
        actual += 1
        max_len = max(max_len, actual)
    else:
        actual = 1

print(max_len)