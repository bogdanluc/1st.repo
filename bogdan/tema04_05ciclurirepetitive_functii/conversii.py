# 1. sa se scrie cate o functie pentru fiecare din conversiile:
# 'C -> 'F, 'C -> 'K, 'F -> 'C, 'K -> 'C

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


print(celsius_to_fahrenheit(5))


def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin


print(celsius_to_kelvin(5))


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / (9 / 5)
    return celsius


print(fahrenheit_to_celsius(5))


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


print(kelvin_to_celsius(5))
