# 6. Sa se scrie o functie pentru rezolvarea ecuatiei de grad 2.
# Parametri de intrare: a, b, c. parametri de iesire: x1, x2.

def ecuatie_grad_2(a, b, c):
    d = b ** 2 - (4 * a * c)
    x = -b / (2 * a)
    x1 = ((-b + d ** (1 / 2)) / (2 * a))
    x2 = ((-b - d ** (1 / 2)) / (2 * a))
    if d < 0:
        print('Ecuatia nu are solutii reale.')
        return None, None
    elif d == 0:
        print('Ecuatia are 2 solutii reale si egale:')
        print(f'x1 = x2 = {x}')
        return x, x
    elif d > 0:
        print('Ecuatia are 2 solutii reale si distincte:')
        return (f'x1: {x1}, x2: {x2}')


print(ecuatie_grad_2(1, 14, 24))
print(ecuatie_grad_2(1, 1, 1))
