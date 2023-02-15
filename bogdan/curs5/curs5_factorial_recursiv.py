# Sa se scrie o functie pentru factorialul unui numar folosind recursivitatea.

def factorial(numar):
    if numar == 1:
        return 1
    else:
        return numar * factorial(numar - 1)


print(factorial(5))