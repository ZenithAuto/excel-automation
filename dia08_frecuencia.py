# dia08_frecuencia.py

palabras = input().split()
freq = {}

for p in palabras:
    if p in freq:
        freq[p] += 1
    else:
        freq[p] = 1

for k in freq:
    print(k, freq[k])