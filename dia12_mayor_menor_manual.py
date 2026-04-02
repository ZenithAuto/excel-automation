nums = list(map(int, input().split()))
mayor = nums[0]
menor = nums[0]

for n in nums:
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n

print(mayor)
print(menor)