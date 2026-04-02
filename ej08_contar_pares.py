nums = list(map(int, input().split()))
pares = 0

for n in nums:
    if n % 2 == 0:
        pares += 1

print(pares)