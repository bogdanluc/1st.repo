# Clasa Dreptunghi
# Atribute: lungime, latime, culoare. Constructor pentru toate atributele
# Metode: ● descrie() ● aria() ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().
class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie_dreptungiul(self):
        print(f'Dreptunghiul are lungimea de {self.lungime}, latimea de {self.latime} si culoarea {self.culoare}')

    def aria_dreptunghiului(self):
        print(f'Aria dreptunghiului cu lungimea de {self.lungime} cm si latimea de {self.latime} cm este: '
              f'{self.lungime * self.latime} cm')

    def perimetrul_dreptunghiului(self):
        print('Perimetrul dreptunghiului este: '
              f'{self.lungime + self.latime + self.lungime + self.latime}')

    def schimba_culoarea(self):
        noua_culoare = 'verde'
        return noua_culoare

un_dreptunghi = Dreptunghi(lungime=0,latime=0,culoare=0)
un_dreptunghi.latime = 3
un_dreptunghi.lungime = 6
un_dreptunghi.culoare = 'rosu'
un_dreptunghi.aria_dreptunghiului()
un_dreptunghi.descrie_dreptungiul()
un_dreptunghi.perimetrul_dreptunghiului()
un_dreptunghi.culoare = un_dreptunghi.schimba_culoarea()
un_dreptunghi.descrie_dreptungiul()
print(un_dreptunghi.culoare)
