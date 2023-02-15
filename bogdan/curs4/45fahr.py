# Sa se scrie o functie care primeste ca parametru de intrare o temperatura in
# grade Fahrenheit, si returneaza echivalentul in grade Celsius

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius

print(fahrenheit_to_celsius(32))
print(fahrenheit_to_celsius(100))