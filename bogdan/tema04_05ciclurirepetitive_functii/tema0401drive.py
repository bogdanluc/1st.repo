# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin',
          'Lăstun', 'Fiat', 'Trabant', 'Opel']
for m in range(len(masini)):
    print(f'Mașina mea preferată este {masini[m]}')

for m in masini:
    print(f'Mașina mea preferată este {m}')

i = 0
while i < len(masini):
    print(f'Mașina mea preferată este {masini[i]}')
    i = i + 1

# 2. Aceeași listă: - Folosește un for else
# În for
# - Modiﬁcă elementele din listă astfel încât să ﬁe scrie cu majuscule, exceptând primul și ultimul.
# În else: - Printează lista.

for m in masini:
    m = m.lower()[0] + m.upper()[1:(len(m)-1)] + m[-1]
    print(m)
else:
    print(m) # incomplet !!!


