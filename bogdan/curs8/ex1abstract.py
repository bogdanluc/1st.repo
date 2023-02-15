import abc
from abc import ABC


class Speakable(ABC):
    @abc.abstractmethod
    def speak(self):
        pass


class Cat(Speakable):
    def speak(self):
        print("Miau!")


class Dog(Speakable):
    def speak(self):
        print("Ham Ham!")


class Crocodile(Speakable):
    def speak(self):
        print("crr mrr")


animals = [Cat(), Dog(), Crocodile()]
for animal in animals:
    animal.speak()