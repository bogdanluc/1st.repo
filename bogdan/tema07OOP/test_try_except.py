try:
    un_intreg = int("abc")  # cod predispus la exceptie
except ValueError:
    print(
        'A aparut eroarea TypeError, ar trebui citita alta valoare de la tastatura!')  # cod pentru afisarea sau tratarea eroorii
else:
    print('Nu a aparut nicio exceptie')