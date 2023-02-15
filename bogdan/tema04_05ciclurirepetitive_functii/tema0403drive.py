# #3. Aceeași listă: Vine un cumpărător care dorește să cumpere un Mercedes.
#    Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes: Printează ‘am găsit mașina dorită de dvs’
#    Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel: Printează ‘Am găsit mașina X. Mai căutam‘

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin',
          'Lăstun', 'Fiat', 'Trabant', 'Opel']

m = 0
while m < len(masini):
    print(masini[m])
    m = m + 1
    if m == masini.index('Mercedes'):
        continue
    print(m)
else:
    print('ds')
