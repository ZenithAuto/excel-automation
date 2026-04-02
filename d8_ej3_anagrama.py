palabra1 = input().lower()
palabra2 = input().lower()

if sorted(palabra1) == sorted(palabra2):
    print("SI")
else:
    print("NO")