def decorator_function(function):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        result = function(*args, **kwargs)
        print("ceva dupa")
        return result

    return inner


@decorator_function
def o_functie_oarecare(p1, p2, *args, **kwargs):
    print(p1, p2, args, kwargs)
    return True


val = o_functie_oarecare(2, 5, 7, a=1, b=3)