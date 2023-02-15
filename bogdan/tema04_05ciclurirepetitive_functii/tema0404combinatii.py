# 4. Sa se scrie o functie care genereaza toate combinatiile posibile
# a-z 0-9 de cate 3 caractere.

def possible_combinations():
    litere = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z',)
    numere = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    literenumere = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    for a in litere:
        for x in numere:
            for i in literenumere:
                print(a, x, i, )


possible_combinations()
