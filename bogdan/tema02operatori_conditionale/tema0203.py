# 3. Veriﬁcă și aﬁșează dacă x este număr pozitiv, negativ sau neutru.


x = int(input('x: '))
if x > 0:
    print(f'{x} este numar pozitiv')
elif x < 0:
    print(f'{x} este numar negativ')
elif x == 0:
    print(f'{x} - numar neutru')
 