numero_secreto = 7

while True:
    n = int(input("Adivina el número: "))
    if n == numero_secreto:
        print("Correcto")
        break
    else:
        print("Intenta otra vez")