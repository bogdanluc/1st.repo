# Fiind data o lista cu numere, sa se dubleze toate numerele divizibile cu 7

lista = [30, 49, 90, 14, 88, 3, 147]
div7 = lista[0]
for div7 in lista:
    if div7 % 7 == 0:
        print(div7)
        div7 = div7 * 2
        print(div7)


lista = [1,5,14,24,28,35,105,21]
lista.sort()
div7 = lista[0]
for div7 in lista:
    if div7 % 7 == 0:
        print(div7)
        lista.append(div7)
        print(lista)
    if div7 == max(lista):
        break
    else:
        print("Stop")