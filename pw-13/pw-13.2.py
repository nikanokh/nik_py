"""
В матрице найти сумму отрицательных элементов в первой трети матрицы.
"""

matrix = [
    [-2, 3, 3, 4, -5],
    [3, 3, 4, -2, -3],
    [-2, 3, 3, 4, -5],
    [3, 13, 4, 12, -3],
    [3, 4, 5, 6, -5]
]

numbers = [num for row in matrix for num in row]
numbers = numbers[:int(len(numbers) / 3)]
numbers = [num for num in numbers if num < 0]

print(sum(numbers))