# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

def return_lungime_caractere(a, b, c):
    nume = a
    prenume = b
    nume_mijlociu = c
    lungime_nume = len(nume) + len(prenume) + len(nume_mijlociu)
    return lungime_nume


print(return_lungime_caractere('Lucaciu', 'Bogdan', 'Sorin'))
