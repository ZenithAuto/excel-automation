def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

opcion = input("suma/resta: ")
a = int(input())
b = int(input())

if opcion == "suma":
    print(suma(a, b))
elif opcion == "resta":
    print(resta(a, b))
else:
    print("Opción inválida")