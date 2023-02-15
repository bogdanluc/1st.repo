# Sa se defineasca functia reduce_price(price_old, price_new),
# care sa confirme ca noul pret nu este mai mic cu 10% decat cel vechi.
# Daca, cumva se intampina caz de eroare, sa se faca raise cu InvalidPriceError

class InvalidPriceError(Exception):
    pass


def reduce_price(price_old, price_new):
    is_valid = price_new <= price_old
    if is_valid:
        return price_new
    else:
        raise InvalidPriceError

if __name__ == '__main__':
    reduce_price(10,5)
    reduce_price(10,13)
