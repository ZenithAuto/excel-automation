n = int(input())
nums = list(map(int, input().split()))

menor = None
segundo = None

for x in nums:
    if menor is None or x < menor:
        if menor != x:
            segundo = menor
        menor = x
    elif x != menor and (segundo is None or x < segundo):
        segundo = x

if segundo is None:
    print(-1)
else:
    print(segundo)