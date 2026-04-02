def promedio(lista):
    return sum(lista) / len(lista)

nums = list(map(int, input().split()))
print(promedio(nums))