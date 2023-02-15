# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

def diferente_numere(x,y):
    if x > y:
        print(f'Primul număr {x} este mai mare decat al doilea nr {y}')
    if x < y:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    if x == y:
        print('Numerele sunt egale')

diferente_numere(3,6)
diferente_numere(36,8)
diferente_numere(9,9)