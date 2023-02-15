# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și Talse dacă nu găsește.

def gaseste_caracterul(z):
    my_string = 'gold rush kid'
    if z in my_string:
        print(True)
    else:
        print(False)

gaseste_caracterul('u')
gaseste_caracterul('a')
