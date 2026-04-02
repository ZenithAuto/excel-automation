nums = list(map(int, input().split()))
impares = 0

for n in nums:
    if n % 2 != 0:
        impares += 1

print(impares)