class Produs:
    def __init__(self):
        self.nume = ''  # proprietate
        self.descriere = ''  # proprietate
        self.pret = 0  # proprietate

    def afisare(self):  # metoda
        print(f'{self.nume} {self.pret}')


un_produs = Produs()
un_produs.nume = 'HP'
un_produs.descriere = 'Pavillion dv5'
un_produs.pret = 899.98
print(un_produs.nume)
un_produs.afisare()