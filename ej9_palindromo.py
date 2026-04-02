palabra = input().lower()

if palabra == palabra[::-1]:
    print("SI")
else:
    print("NO")