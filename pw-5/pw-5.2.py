"""
Описать функцию Mean(параметры), вычисляющую среднее арифметическое
AMean = (X+Y)/2 и среднее геометрическое GMean = y/X Y двух положительных
чисел X и Y. С помощью этой функции найти среднее арифметическое и среднее
геометрическое для пар (A, B), (A, C), (A, D), если даны A, B, C, D.

"""
import math


def g_mean(n, m):
    return math.sqrt(n * m)


def a_mean(n, m):
    return (n + m) / 2


while True:
    try:
        a = int(input('Введите число a: '))
        b = int(input('Введите число b: '))
        c = int(input('Введите число c: '))
        d = int(input('Введите число d: '))

        print(f'Среднее арифметическое для a и b: {a_mean(a, b)}, a и c: {a_mean(a, c)}, a и d: {a_mean(a, d)},')
        print(f'Среднее арифметическое для a и b: {g_mean(a, b)}, a и c: {g_mean(a, c)}, a и d: {g_mean(a, d)},')
    except ValueError:
        print("Вводите целые числа")

