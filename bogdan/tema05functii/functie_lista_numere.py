# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive

# def lista_numere(*args):
#     for i in args:
#         if i >= 0:
#             print(i)
#
# lista_numere(-2,5,-20,4,756,-324,843)

def lst_nr(*args):
    lista = []
    for i in args:
        if i >= 0:
            lista.append(i)
            print(lista)


lst_nr(-2, 5, -20, 4, 756, -324, 843, 3, 6, 1)
