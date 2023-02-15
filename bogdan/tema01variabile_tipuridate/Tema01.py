# #ex.1. radicalul
a = input('radicalul numarului: ')
a = int(a)
print(a**(1/2))

#ex.2. rata lunara
credit = 3300
perioada_luni = 12
print(credit / perioada_luni)

#ex.3. media armonica
a, b, c = int(input('x')), int(input('y')), int(input('z'))
print(2/((1/a)+(1/b)+(1/c)))

#ex.4 media ponderata
a, b, c = 7, 5, 9
p, q, r = 3, 2, 7
print((a*p+b*q+c*r)/(p+q+r))

#ex.5, a*x+b=0
a = 3
b = 6
x = ((0 - b)/a)
print(x)
print(a*x+b==0) # => True

#ex.6. a * x ** 2 + b * x + c = 0

a = 1
b = 14
c = 24
d=b**2-(4*a*c)
x = -b/(2*a)
x1 = ((-b+d**(1/2)) / (2*a))
x2 = ((-b-d**(1/2)) / (2*a))
if d< 0:
    print('Ecuatia nu are solutii reale.')
elif d==0:
    print('Ecuatia are 2 solutii reale si egale:')
    print(f'x1 = x2 = {x}')
elif d > 0:
    print('Ecuatia are 2 solutii reale si distincte:')
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')

#ex.7. 25% din 50%

a = 99
print(a/2/4)