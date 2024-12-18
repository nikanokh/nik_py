"""
Составить функцию, которая напечатает сорок любых символов.
"""

import random


def print_rnd_sym():
    random.random()
    [print(int(random.uniform(0, 10)) // 1, end='') for _ in range(0, 40)]


print_rnd_sym()

