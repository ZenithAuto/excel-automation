contador = 0

while True:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 0:
        contador += 1

print(contador)