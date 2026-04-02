nums = list(map(int, input("Números: ").split()))

cantidad = len(nums)

suma_total = sum(nums)

mayor = max(nums)

menor = min(nums)

pares = 0
impares = 0
suma_pares = 0
suma_impares = 0

for n in nums:
    if n % 2 == 0:
        pares += 1
        suma_pares += n
    else:
        impares += 1
        suma_impares += n

print("Cantidad:", cantidad)
print("Suma total:", suma_total)
print("Mayor:", mayor)
print("Menor:", menor)
print("Pares:", pares)
print("Impares:", impares)
print("Suma pares:", suma_pares)
print("Suma impares:", suma_impares)

if pares > impares:
    print("Resultado: HAY MÁS PARES")
elif impares > pares:
    print("Resultado: HAY MÁS IMPARES")
else:
    print("Resultado: HAY LA MISMA CANTIDAD")