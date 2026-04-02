n = int(input())

if n < 2:
    print("NO")
else:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break

    if primo:
        print("SI")
    else:
        print("NO")