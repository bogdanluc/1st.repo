class NumberIterator:
    def __init__(self, start=0):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        temp = self.current
        self.current += 1
        return temp


iterator_numere = NumberIterator()
un_iterator = iter(iterator_numere)
print(next(un_iterator))
print(next(un_iterator))
print(next(un_iterator))
print(next(un_iterator))
print(next(un_iterator))
print(next(un_iterator))
print(next(un_iterator))
