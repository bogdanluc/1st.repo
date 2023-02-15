# Fiind data o tupla de elemente, sa se calculeze media lor aritmetica.

tupla = (5, 6, 8, 3, 11)
suma = 0
for element in tupla:
    suma += element
ma = suma / len(tupla)
print(ma)

print(sum(tupla) / len(tupla))

