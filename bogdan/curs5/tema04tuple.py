def convert_to_tuple(*numbers):
    squares = []
    cubes = []
    for number in numbers:
        if perfect_square(number):
            squares.append(number)
        elif perfect_cube(number):
            cubes.append(number)
    return squares, cubes


def perfect_square(nr):
    radical = nr ** 0.5
    is_int = radical == int(radical)
    return is_int


def perfect_cube(nr):
    radical = nr ** 1 / 3
    is_int = radical == int(radical)
    return is_int

print(convert_to_tuple(2,3,27,16))
