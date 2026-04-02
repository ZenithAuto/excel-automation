def mayor(lista):
    m = lista[0]
    for x in lista:
        if x > m:
            m = x
    return m

nums = list(map(int, input().split()))
print(mayor(nums))