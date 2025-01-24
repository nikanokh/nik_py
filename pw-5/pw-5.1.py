"""
Составить функцию, которая напечатает сорок любых символов.
"""

import random


def print_rnd_sym():
    [print(chr(int(random.uniform(1, 8000)) // 1), end='') for _ in range(0, 40)]


print_rnd_sym()

