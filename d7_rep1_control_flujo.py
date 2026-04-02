n = int(input())

if n > 0:
    if n % 2 == 0:
        print("POSITIVO PAR")
    else:
        print("POSITIVO IMPAR")
elif n < 0:
    if n % 2 == 0:
        print("NEGATIVO PAR")
    else:
        print("NEGATIVO IMPAR")
else:
    print("CERO")