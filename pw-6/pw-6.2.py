"""
Дан список размера N. Найти номера тех элементов список, которые больше своего
левого соседа, и количество таких элементов. Найденные номера выводить в
порядке их убывания.
"""


while True:
    try:
        nums = []
        [nums.append(int(input(f'[{i}] = ')))
         for i in range(int(input('Введите длину списка: ')))]
        N = len(nums)

        arr = []
        [arr.append(i + 1) if nums[i] < nums[i + 1] else print(end='')
         for i in range(len(nums) - 1)]

        print(f'Количество элементов соответствующих условию: {len(arr)}')
        [print(i, end=' ') for i in arr[::-1]]
        print()
    except ValueError:
        print("Вводите целые числа")