# 1. Даны три целых числа. Определить у какого числа больше сумма цифр. Вывод
# результата предусмотреть в основной программе. Расчет суммы цифр оформить в
# функции.
def sum_el(n):
    s = str(n)
    summa = 0
    for c in s:
        summa += int(c)
    return summa


def P(a, b):
    return (a + b) * 2


def S(a, b):
    return a * b


n0 = int(input('Введите первое число'))
n1 = int(input('Введите второе число'))
n2 = int(input('Введите третье число'))

print('Первое') if sum_el(n2) < sum_el(n0) > sum_el(n1) else \
    print('Второе') if sum_el(n1) > sum_el(n2) else \
        print('Третье')

# 2. Рассчитать и вывести периметр и площадь прямоугольника. Расчеты оформить в
# функции.

a = int(input('Введите сторону a: '))
b = int(input('Введите сторону b: '))
print(f'P = {P(a, b)}, S = {S(a, b)}')

# 3. Написать программу, подсчитывающую количество цифр числа, используя для
# этого функцию.
print(f'Длина следующего числа {len(str(int(input('Введите число: '))))} цифр')
