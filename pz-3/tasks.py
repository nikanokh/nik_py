# Add 1: Ввести 2 числа. Если их произведение отрицательно, умножить его на 8, в противном
# случае увеличить его в 1.5 раза.
print('task 1')

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

product = num1 * num2

if product < 0:
    result = product * 8
else:
    result = product * 1.5

print(result)

# Add 2: Вести число. Если оно четное, разделить его на 4, если нечетное - умножить на 5.
print('task 2')

num = int(input("Введите число: "))

if num % 2 == 0:
    result = num / 4
else:
    result = num * 5

print(result)

# Add 3: Ввести двухзначное число. Если сумма цифр числа четная, то увеличить число на 2,
# в противном случае уменьшить на 2.
print('task 3')

num = int(input("Введите двухзначное число: "))

a = num // 10
b = num % 10

if (a + b) % 2 == 0:
    num += 2
else:
    num -= 2

print(num)

# Add 4: Дано целое число. Если оно является положительным, то прибавить к нему 20, в
# противном случае вычесть из него 5.
print('task 4')

num = int(input("Введите целое число: "))

if num > 0:
    num += 20
else:
    num -= 5

print(num)

# Add 5: Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2.
print('task 5')
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
summa = num1 + num2
if summa % 5 == 0:
    summa += 1
else:
    summa -= 1

print(summa)

