# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False

def numar_set(a, set):
    nr = a
    if nr not in set:
        print(f'am adaugat numărul nou în set')
        return True
    if nr in set:
        print(f'nu am adaugat numărul în set. Acesta există deja')
        return False


set = {3, 5, 9, 2}

numar_set(3, set)
numar_set(7, set)
print(numar_set(2, set))
print(numar_set(4, set))
