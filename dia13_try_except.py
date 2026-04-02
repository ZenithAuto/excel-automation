try:
    n = int(input())
    print(100 // n)
except ZeroDivisionError:
    print("ERROR")