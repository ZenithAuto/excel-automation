nums = list(map(int, input().split()))
ordenada = True

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        ordenada = False
        break

print("SI" if ordenada else "NO")