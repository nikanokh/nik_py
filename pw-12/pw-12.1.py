"""
Организовать и вывести последовательность А из n чисел (n - четное). Из
последовательности А получить две последовательности В и С: в последовательности В –
первая половина элементов А, в С – вторая половина элементов А. Найти произведение
соответствующих элементов последовательностей В и С. Найти среднее арифметической
полученной последовательности.
"""

import random

a = [random.randint(-100, 100) for i in range(20)]
print(a)

b, c = a[:len(a) // 2], a[len(a) // 2:]
# bc = [b[i] * c[i] for i in range(0, len(b))]
bc = list(map(lambda x, y: x * y, b, c))
print(bc)

mean = sum(bc) / len(bc)
print(mean)

l = [list]
