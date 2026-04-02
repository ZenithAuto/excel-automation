# dia08_palindromo.py

s = input().lower()

if s == s[::-1]:
    print("SI")
else:
    print("NO")