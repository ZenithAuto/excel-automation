nums = list(map(int, input().split()))
suma = 0

for i in range(len(nums)):
    if i % 2 == 0:
        suma += nums[i]

print(suma)