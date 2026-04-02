def promedio(lista):
    return sum(lista) / len(lista)

n = int(input())
nums = list(map(int, input().split()))
print(promedio(nums))