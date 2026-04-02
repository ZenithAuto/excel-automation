numeros = list(map(int, input().split()))

mayor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n

print(mayor)