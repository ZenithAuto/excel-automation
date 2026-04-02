suma = 0
contador = 0

while True:
    n = int(input())
    if n == 0:
        break
    suma += n
    contador += 1

if contador > 0:
    print(suma / contador)