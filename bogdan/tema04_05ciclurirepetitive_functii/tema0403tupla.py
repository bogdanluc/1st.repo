# 3. Sa se scrie o functie care primeste ca parametru o lista cu numere,
# si returneaza o tupla cu 2 liste formate din patratele, respectiv cuburile perfecte din lista initiala.

def lista_to_tupla(a, b, c):
    lista_patrate = [a ** 2, b ** 2, c ** 2]
    lista_cuburi = [a ** 3, b ** 3, c ** 3]
    return (lista_patrate, lista_cuburi)


print(lista_to_tupla(2, 5, 7))
