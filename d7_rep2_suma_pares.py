n = int(input())
numeros = list(map(int, input().split()))

suma = 0

for num in numeros:
    if num % 2 == 0:
        suma += num

print(suma)