frase = input().lower()

limpia = ""

for c in frase:
    if c.isalpha():
        limpia += c

if limpia == limpia[::-1]:
    print("SI")
else:
    print("NO")