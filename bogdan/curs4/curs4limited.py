def is_prime(nr):
    for i in range(2, nr):
        if nr % i == 0:
            return False
    return True


def generate_prime():
    for i in range(2, 101):
        if is_prime(i):
            print(i)


generate_prime()


def generate_primes_limit(limit):
    primes_found = 0
    nr = 2
    while primes_found < 100:
        if is_prime(nr):
            print(nr)
            primes_found += 1
        nr += 1


generate_primes_limit(51)
