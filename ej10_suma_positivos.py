nums = list(map(int, input().split()))
suma = 0

for n in nums:
    if n > 0:
        suma += n

print(suma)