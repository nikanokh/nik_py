"""
Вариант 2.
1. Даны два целых числа A и B (A < B). Вывести в порядке убывания все целые числа,
расположенные между A и B (не включая числа A и B), а также количество N этих
чисел.
2. Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от
деления определить, имеются ли в записи числа N нечетные цифры. Если имеются,
то вывести TRUE, если нет — вывести FALSE.

"""
A = int(input("Введите A: "))
B = int(input("Введите B: "))
count = 0
for i in range(B, A - 1, -1):
    print(i)
    count += 1
print("Количество чисел:", count)
