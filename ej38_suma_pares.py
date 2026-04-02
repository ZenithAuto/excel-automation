numeros = list(map(int, input().split()))
suma = 0

for n in numeros:
    if n % 2 == 0:
        suma += n

print(suma)