# Sa se defineasca clasa Person cu proprietatile first_name, last_name, ssn si metoda __str__

class Person:
    def __init__(self, first_name, last_name, ssn):
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.ssn}'


ion = Person('Ion', 'Pop', '123')
print(ion)
