'''
1.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''

x = int(input('x => '))
if (x) >= 1000:
    print('x are minim 4 cifre')
elif (x) < 1000:
    print('x are mai putin de 4 cifre')
