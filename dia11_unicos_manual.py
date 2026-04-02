nums = list(map(int, input().split()))
unicos = []

for x in nums:
    if x not in unicos:
        unicos.append(x)

print(unicos)