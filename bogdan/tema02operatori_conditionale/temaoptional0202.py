#2.Verifică dacă x are exact 6 cifre.

x = int(input('x => '))
if (100000 < x < 999999):
    print('x are exact 6 cifre')
elif x < 100000:
    print('x are mai putin de 6 cifre')
elif x > 999999:
    print('x are mai mult de 6 cifre')

