"""
В матрице найти минимальный и максимальные элементы.
"""

matrix = [
    [-2, 3, 3, 4, 5],
    [3, 3, 4, 12, 6],
    [3, 4, 5, 6, 0]
]

numbers = [num for row in matrix for num in row]

print(min(numbers), max(numbers))