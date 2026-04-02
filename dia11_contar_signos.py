n = int(input())
nums = list(map(int, input().split()))

pos = neg = cer = 0

for x in nums:
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
    else:
        cer += 1

print(pos)
print(neg)
print(cer)