#7.
# x și y (int)
# Veriﬁcă și aﬁșează dacă sunt egale, dacă nu aﬁșează care din ele este mai
# mare.


x = int(input('x: '))
y = int(input('y: '))
if x == y:
    print('numere egale')
elif x > y:
    print(f'{x} este numarul mai mare')
elif x < y:
    print(f'{y} este numarul mai mare')