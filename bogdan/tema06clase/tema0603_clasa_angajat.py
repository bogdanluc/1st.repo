# 3. Clasa Angajat
# Atribute: nume, prenume, salariu # Constructor pt toate atributele
# Metode:
# ● descrie() ● nume_complet() ● salariu_lunar() ● salariu_anual() ● marire_salariu(procent)

class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Angajatul {self.prenume} {self.nume} castiga {self.salariu} lunar')

    def nume_complet(self):
        print(f'Numele complet al angajatului {self.prenume} este: {self.nume}, {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul lunar este: {self.salariu} lei')

    def salariu_anual(self):
        print(f'Salariul anual al angajatului {self.prenume} {self.nume} este {self.salariu * 12} lei')

    def marire_salariu(self):
        print(f'Salariul angajatului {self.nume} {self.prenume} va creste de la'
              f' {self.salariu} cu 15% si va fii: {round(self.salariu * 1.15)} lei')


salariat_1 = Angajat('Pop', 'Dan', 3200)
salariat_2 = Angajat('Doe', 'John', 6800)
salariat_3 = Angajat('Smith', 'Peter', 5400)
salariat_1.descrie()
salariat_2.descrie()
salariat_3.descrie()
salariat_1.marire_salariu()
salariat_3.nume_complet()
salariat_2.salariu_anual()
