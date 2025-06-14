"""
Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
Добавьте методы для вычисления среднего балла и определения, является ли студент
отличником.
"""


class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)

    def is_excellent(self):
        return self.average_marks() == 5