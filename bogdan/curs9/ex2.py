def numbers(from_, to):
    for number in range(from_, to + 1):
        yield number


my_numbers = numbers(1, 100)
print(my_numbers)
print(list(my_numbers))