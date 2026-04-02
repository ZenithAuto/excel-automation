def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

op = input("suma/resta: ")
a = int(input())
b = int(input())

if op == "suma":
    print(suma(a, b))
elif op == "resta":
    print(resta(a, b))