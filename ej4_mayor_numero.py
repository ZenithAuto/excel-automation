mayor = None

while True:
    n = int(input())
    if n == 0:
        break
    if mayor is None or n > mayor:
        mayor = n

print(mayor)