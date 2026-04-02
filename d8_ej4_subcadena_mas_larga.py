cadena = input()

max_sub = ""
actual = cadena[0]

for i in range(1, len(cadena)):
    if cadena[i] > cadena[i - 1]:
        actual += cadena[i]
    else:
        if len(actual) > len(max_sub):
            max_sub = actual
        actual = cadena[i]

if len(actual) > len(max_sub):
    max_sub = actual

print(max_sub)