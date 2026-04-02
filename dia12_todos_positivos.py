nums = list(map(int, input().split()))
todos = True

for n in nums:
    if n <= 0:
        todos = False
        break

print("SI" if todos else "NO")