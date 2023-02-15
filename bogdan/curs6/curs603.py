#sa se defineasca o functie read_float, care se asigura
# ca userul introduce un float de la tastatura.

def read_float():
    val = input("Introduceti un numar float:")
    try:
        result = float(val)
    except ValueError:
        result = read_float()
    return result


if __name__ == '__main__':
    print(read_float())