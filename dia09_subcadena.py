cadena = input()
sub = input()

contador = 0
for i in range(len(cadena) - len(sub) + 1):
    if cadena[i:i+len(sub)] == sub:
        contador += 1

print(contador)