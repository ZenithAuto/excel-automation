while True:
    n = int(input("Número (negativo para salir): "))
    if n < 0:
        break
    print("Número válido:", n)

print("Saliste del bucle")