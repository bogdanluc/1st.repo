# Sa se scrie o functie care calculeaza media armonica
# a oricator parametri de intrare obligatorii (numere).

def media_armonica(*args):
    numarator = len(args)
    numitor = 0
    for value in args:
        numitor += 1 / value
    ma = numitor / numarator
    return ma


print(media_armonica(1, 2, 3))
