import abc
from abc import ABC, abstractmethod


class Classrooms(ABC):
    @abstractmethod
    def classroom(self):
        pass


class Students(Classrooms):
    def __init__(self, student_name, class_name, year):
        self.student_name = student_name
        self.class_name = class_name
        self.year = year

    def classroom(self):
        return self.student_name, self.class_name, self.year


class Teachers(Classrooms):
    def __init__(self, teachers_name, subject):
        self.teachers_name = teachers_name
        self.subject = subject

    def classroom(self):
        return self.teachers_name, self.subject


class Grades(Classrooms):
    __grade = 9

    def get_grade(self):
        return self.__grade

    def set_grade(self, average_grade):
        self.__grade = average_grade

    def __hidden(self):
        pass

    def classroom(self):
        return


the_classrooms = [Students('Andrei', 'B', 9),
                  Students('Dan', 'D', 7),
                  Teachers('Pop', 'English'),
                  ]
for a_classroom in the_classrooms:
    print(a_classroom.classroom())
