def es_par(n):
    if n % 2 == 0:
        return "par"
    else:
        return "impar"

n = int(input())
print(es_par(n))