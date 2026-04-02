n = int(input())
numeros = list(map(int, input().split()))

# Contamos cuántos números tienen una frecuencia de aparición igual a 1
unicos = [x for x in numeros if numeros.count(x) == 1]

print(len(unicos))