a = 1
b = 3
c = 4
d = b ** 2 - (4 * a * c)
x = -b / (2 * a)
x1 = ((-b+d**(1/2)) / (2*a))
x2 = ((-b-d**(1/2)) / (2*a))
if d < 0:
    print('Ecuatia nu are solutii reale.')
elif d == 0:
    print('Ecuatia are 2 solutii reale si egale:')
    print(f'x1 = x2 = {x}')
elif d > 0:
    print('Ecuatia are 2 solutii reale si distincte:')
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
