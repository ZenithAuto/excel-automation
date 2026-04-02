while True:
    n = int(input("Número (0 para salir): "))
    if n == 0:
        break
    if n < 0:
        continue
    print("Número positivo:", n)