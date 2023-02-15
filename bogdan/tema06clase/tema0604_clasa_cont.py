# 4.Clasa Cont
# Atribute: iban, titular_cont, sold - Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
#  ● debitare_cont(suma)  ● creditare_cont(suma)

class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')

    def debitare_cont(self):
        print(f'Titularul {self.titular_cont} a retras suma 300 lei iar acum soldul este '
              f'{self.sold - 300} lei')

    def creditare_cont(self):
        print(f'Titularul a alimentat contul cu suma de 700 lei iar acum soldul este'
              f' {self.sold + 700}')

titular1 = Cont(436658, 'Petrescu Geanina', 7100)
titular2 = Cont(123098, 'Pop Ioana', 3300)
titular1.afisare_sold()
titular2.afisare_sold()
titular1.debitare_cont()

titular1.creditare_cont()
