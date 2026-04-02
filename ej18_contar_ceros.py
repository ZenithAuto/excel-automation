nums = list(map(int, input().split()))
c = 0

for n in nums:
    if n == 0:
        c += 1

print(c)