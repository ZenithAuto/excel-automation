numeros = list(map(int, input().split()))
print(all(n % 2 == 0 for n in numeros))