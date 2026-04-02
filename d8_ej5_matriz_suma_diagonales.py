n = int(input())

matriz = []

for _ in range(n):
    fila = list(map(int, input().split()))
    matriz.append(fila)

diag_principal = 0
diag_secundaria = 0

for i in range(n):
    diag_principal += matriz[i][i]
    diag_secundaria += matriz[i][n - 1 - i]

print(diag_principal)
print(diag_secundaria)