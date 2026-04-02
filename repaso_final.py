nums = list(map(int, input("Números: ").split()))

print("Suma:", sum(nums))
print("Mayor:", max(nums))

for x in nums:
    if x % 2 == 0:
        print(x, "PAR")
    else:
        print(x, "IMPAR")