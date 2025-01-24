"""
Известно, что X кг шоколадных конфет стоит A рублей, а Y кг ирисок
стоит B рублей. Определить, сколько стоит 1 кг шоколадных конфет, 1 кг ирисок, а также
во сколько раз шоколадные конфеты дороже ирисок.
"""

while True:
    try:
        x = float(input('Введите число X: '))
        a = float(input('Введите число A: '))
        y = float(input('Введите число Y: '))
        b = float(input('Введите число B: '))
        price_ch_candy = a/x
        price_toffee = b/y
        coefficient_diff = price_ch_candy/price_toffee

        print(f'1 кг шоколадных конфет стоит: {price_ch_candy} руб.')
        print(f'1 кг ирисок стоит: {price_toffee} руб.')
        print(f'Шоколадные конфеты дороже ирисок в {round(coefficient_diff, 4)} раз')
    except ZeroDivisionError:
        print('Количество не может быть нулевым')
    except TypeError:
        print('Вводите числа')

