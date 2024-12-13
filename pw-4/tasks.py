import math

# Task 1: Сумма и количество отрицательных чисел
print("Task 1:")
numbers = [float(input("Введите число {}: ".format(i + 1))) for i in range(4)]
negative_count = sum(1 for num in numbers if num < 0)
negative_sum = sum(num for num in numbers if num < 0)
print("Сумма отрицательных чисел:", negative_sum)
print("Количество отрицательных чисел:", negative_count)
print()

# Task 2: Количество четных чисел
print("Task 2:")
numbers = [int(input("Введите число {}: ".format(i + 1))) for i in range(4)]
even_count = sum(1 for num in numbers if num % 2 == 0)
print("Количество четных чисел:", even_count)
print()

# Task 3: Квадраты и кубы чисел от 2 до 5
print("Task 3:")
for i in range(2, 6):
    print(f"Число: {i}, Квадрат: {i**2}, Куб: {i**3}")
print()

# Task 4: Сумма факториалов
print("Task 4:")
n = int(input("Введите n (n > 1): "))
factorial_sum = sum(math.factorial(i) for i in range(1, n + 1))
print("S =", factorial_sum)
print()

# Task 5: Среднее арифметическое
print("Task 5:")
N = int(input("Введите количество чисел: "))
numbers = [float(input("Введите число {}: ".format(i + 1))) for i in range(N)]
average = sum(numbers) / N
print("Среднее арифметическое:", average)
print()

# Task 6: Количество нулей
print("Task 6:")
N = int(input("Введите количество чисел: "))
numbers = [float(input("Введите число {}: ".format(i + 1))) for i in range(N)]
zero_count = sum(1 for num in numbers if num == 0)
print("Количество чисел равных нулю:", zero_count)
print()

# Task 7: Числа от A до B в порядке убывания
print("Task 7:")
A = int(input("Введите A: "))
B = int(input("Введите B: "))
count = 0
for i in range(B, A - 1, -1):
    print(i)
    count += 1
print("Количество чисел:", count)
print()

# Task 8: Сумма чисел от A до B
print("Task 8:")
A = int(input("Введите A: "))
B = int(input("Введите B: "))
total_sum = sum(i for i in range(A, B + 1))
print("Сумма чисел от A до B:", total_sum)
print()

# Task 9: Количество элементов арифметической прогрессии
print("Task 9:")
a1 = 1
d = 3
count = 0
for i in range(10, 30):
    if (i - a1) % d == 0:
        count += 1
print("Количество элементов арифметической прогрессии:", count)
print()

# Task 10: Первые N чисел Фибоначчи и количество четных
print("Task 10:")
N = int(input("Введите N (N ≥ 3): "))
fib = [0, 1]
for i in range(2, N):
    fib.append(fib[-1] + fib[-2])
even_count = sum(1 for num in fib if num % 2 == 0)
print("Первые N чисел Фибоначчи:", fib)
print("Количество четных чисел:", even_count)
print()

# Task 11: Деление элементов арифметической прогрессии на 2
print("Task 11:")
a1 = 1
d = 3
n = 10  # Количество элементов
for i in range(n):
    ai = a1 + i * d
    print(round(ai / 2))