# problema cu dalmatienii
for i in range(1,102):
    print(f'dalmatianul {i}')

numere = [3,7,10,20,30]
#parcurgere lista cu for prin intermediul indexului
for i in range(0, len(numere)):
    print(f'indexul este {i}')
    print(f'numarul este {numere[i]}')

#for each
 # suma numerelor
s=0
for numar in numere:
    print(f'numarul curent este {numar}')
    s=s+numar
    print(f'suma este {s}')

# de cate ori apare 3 in [3,2,3,5,3,]