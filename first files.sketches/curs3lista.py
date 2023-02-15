# Fiind data o lista cu elemente, sa se afle valoarea minima / maxima.
# Hint: sa mearga si cu numere negative.
a = [5, 7, 1, -1, 9]
minim = a[0]
for element in a:
    if element < minim:
        minim = element
print(minim)

a = [5, 7, 1, -1, 9]
maxim = a[0]
for element in a:
    if element > maxim:
        maxim = element
print(maxim)
print(min(a))
print(max(a))
