n = int(input())

resultado = []
for i in range(n, -1, -1):
    resultado.append(str(i))

print(" ".join(resultado))