"""
1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Исходные данные:
Количество элементов:
Максимальный элемент:
Произведение элементов меньших 0 в первой половине:
"""

import random

file = open('info.txt', 'w')
data_str = ''
for i in range(20):
    data_str += str(random.randint(-100, 100)) + ' '
file.write(data_str)
file.close()


file = open('info.txt')
data = file.readline()

data_str = list(data.split())
data_int = [int(i) for i in data_str]

data_len = len(data_int)
data_max = max(data_int)

product = 1
for i in data_int[:int(data_len/2)]:
    if i < 0:
        product *= i

string = f"""Исходные данные: {data}
Количество элементов: {data_len}
Максимальный элемент: {data_max}
Произведение элементов меньших 0 в первой половине: {product}"""

file = open('new.txt', 'w', encoding='UTF-8')
file.write(string)
file.close()
