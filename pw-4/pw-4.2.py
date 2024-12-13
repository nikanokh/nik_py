"""
2. Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от
деления определить, имеются ли в записи числа N нечетные цифры. Если имеются,
то вывести TRUE, если нет — вывести FALSE.
"""


N = int(input("Введите целое число N (>0)"))
c = 0
while True:
    digit = N % 10**(c+1) // 10**c
    print(digit)
    if digit == 0:
        print(False)
        break
    else:
        if digit % 2 == 1:
            print(True)
            break
        else:
            c += 1
