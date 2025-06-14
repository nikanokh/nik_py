"""
Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
"Человек". Каждый класс должен иметь метод, который выводит информацию о
поле объекта
"""


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self._gender = gender

    def get_gender(self):
        print(f"Пол: {self._gender}")


class Man(Human):
    def __init__(self, name, age):
        super().__init__(name, age, gender="Мужской")


class Woman(Human):
    def __init__(self, name, age):
        super().__init__(name, age, gender="Женский")


m = Man('Jon', 18)
m.get_gender()

w = Woman('Jane', 20)
w.get_gender()
