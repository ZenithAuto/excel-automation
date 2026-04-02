menor = None

while True:
    n = int(input())
    if n == 0:
        break
    if menor is None or n < menor:
        menor = n

print(menor)