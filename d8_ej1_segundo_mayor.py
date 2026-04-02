n = int(input())
numeros = list(map(int, input().split()))

unicos = list(set(numeros))
unicos.sort()

if len(unicos) < 2:
    print("NO")
else:
    print(unicos[-2])