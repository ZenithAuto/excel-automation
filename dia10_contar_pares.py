n = int(input())
nums = list(map(int, input().split()))

contador = 0
for x in nums:
    if x % 2 == 0:
        contador += 1

print(contador)