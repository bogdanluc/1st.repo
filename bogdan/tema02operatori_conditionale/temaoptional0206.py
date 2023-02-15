#6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# Citiți de la tastatură un int x
# Afișează stringul fără ultimele x caractere

coral = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('=> '))
coralx = coral[: - x]
print(coralx)