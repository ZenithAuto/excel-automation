nums = list(map(int, input().split()))
resultado = []

for n in nums:
    if n >= 0:
        resultado.append(n)

print(resultado)