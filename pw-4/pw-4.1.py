"""
1. Даны два целых числа A и B (A < B). Вывести в порядке убывания все целые числа,
расположенные между A и B (не включая числа A и B), а также количество N этих
чисел.
"""

while True:
    try:
        A = int(input("Введите A: "))
        B = int(input("Введите B: "))
        count = 0
        for i in range(B, A - 1, -1):
            count += 1
        print("Количество чисел:", count)
    except ValueError:
        print("Вводите целые числа")
