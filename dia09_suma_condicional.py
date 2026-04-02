suma = 0

while True:
    n = int(input())
    if n == 0:
        break
    if n > 0 and n % 2 == 0:
        suma += n

print(suma)