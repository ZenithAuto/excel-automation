n = int(input())
numeros = list(map(int, input().split()))

if numeros:
    promedio = sum(numeros) / len(numeros)
    mayores = [str(x) for x in numeros if x > promedio]
    
    if mayores:
        print(" ".join(mayores))