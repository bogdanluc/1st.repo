#Sa se scrie o functie care primeste un numar ca parametru
# si returneaza True daca este prim, si False daca nu este prim.

def is_prime(nr):
    for i in range(2, nr):
        if nr % i == 0:
            return False
    return  True

print(is_prime(3))
print(is_prime(4))
print(is_prime(17))
print(is_prime(20))