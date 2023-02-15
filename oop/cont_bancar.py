class ContBancar:
    #constructor
    def __init__(self, titularCont, iban):
        #atribute, fields
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.pin = 7777
        self.incercariactivare = 0

    def interogareSold(self):
        print(f'Titular {self.titularCont}')
        print(f'iban {self.iban}')
        print(f'sold {self.sold}')
        print(f'activ {self.activ}')
        print(f'incercari activare {self.incercariactivare}')
        print('---------------------')

    def activareCont(self, pin_utilizator):
        print(f'Buna {self.titularCont}')
        if pin_utilizator == self.pin:
            print('Card activat')
            self.activ = True
        else:
            print('PIN gresit')
            self.incercariactivare +=1  # = incercariactivare +1
    def alimentareCont(self, suma):
        self.sold =+ suma
        print(f'Ati alimentat suma: {suma}')
        print(f"aveti in cont: {self.sold}")
    def plataCard(self, suma):
        if suma <= self.sold:
            self.sold -= suma
            print(f'Ati cheltuit {suma}')
            print(f'Aveti in cont {self.sold}')
        else:
            print('fonduri insuficiente')
