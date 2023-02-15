''' Ex. 2.
Variabila string - tip de date delimitat de ' ' sau " " in care poti folosi orice caractere,
are valoare unica care poate fii suprascrisa.
ex:
'''
prenume = 'Bogdan'
nume = 'Lucaciu'
print(nume +' ' + prenume)

#Ex.4.
# Declar si initializez diferite tipuri de variabile

produs = 'ciocolata' #string
pret = 60 #integer
calorii = 545.601 #float
expirata = False #boolean

print(f'{produs}  la {pret}  lei are  {calorii} calorii')
print(expirata == False) # raspunsul este true

#Ex.6


# for i in i:
#     i=1;
#     i<20;
#     i=i+3;
#     print(i)

for i in range(1, 20, 3):
    print(i) # functia for - 1: numar start, 20: - numar final, 3 - parcurge numerele din 3 in 3
