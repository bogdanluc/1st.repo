# Sa se scrie o functie care primeste ca parametru o temperatura
# in grade Celsius, si intoarce echivalentul in grade Kelvin

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin


print(celsius_to_kelvin(0))
print(celsius_to_kelvin(100))
