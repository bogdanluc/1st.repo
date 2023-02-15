from abc import ABC, abstractmethod


class AsRow(ABC):
    @abstractmethod
    def as_row(self) -> tuple:
        pass


class Product(AsRow):
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def as_row(self) -> tuple:
        return self.name, self.price, self.stock


class Service(AsRow):

    def __init__(self, title, description, active):
        self.title = title
        self.description = description
        self.active = active

    def as_row(self) -> tuple:
        return self.title, self.description, self.active

class Shop(AsRow):

    def __init__(self, store, city, store_hours):
        self.store = store
        self.city = city
        self.store_hours = store_hours

    def as_row(self) -> tuple:
        return self.store, self.city, self.store_hours

def list_objects(objects):
    for obj in objects:
        print(f'|{obj.as_row()[0]:<25}|{obj.as_row()[1]:^25}|{obj.as_row()[2]:>25}|')


products = [
    Product('mere', 99.95, 100),
    Product('pere', 199.95, 150),
    Product('prune', 299.95, 1000),
    Service('transport', 'ieftin', True),
    Service('retur', 'tot timpul', False),
    Shop('Central', 'Cluj-Napoca', '09:00 - 21:00'),
]
list_objects(products)