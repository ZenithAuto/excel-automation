# dia08_segundo_mayor.py

n = int(input())
nums = list(map(int, input().split()))

mayor = -10**18
segundo = -10**18

for x in nums:
    if x > mayor:
        segundo = mayor
        mayor = x
    elif x > segundo and x != mayor:
        segundo = x

print(segundo)