# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode: ● descrie_cerc() - va PRINTA culoarea și raza, ● aria() - va RETURNA aria
# ● diametru(), ● circumferinta()
import math


class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Cercul are culoarea {self.culoare} si raza {self.raza}')

    def aria_cercului(self):
        return math.pi * self.raza ** 2

    def diametrul_cercului(self):
        return 2 * self.raza

    def circumferinta_cercului(self):
        return 2 * self.raza * math.pi


if __name__ == '__main__':
    un_cerc = Cerc()
    un_cerc.diametrul_cercului()
    un_cerc.circumferinta_cercului()
    un_cerc.descrie_cerc()
    un_cerc.aria_cercului()
