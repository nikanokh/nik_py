"""
Дан список размера N. Обнулить элементы списка, расположенные между его
минимальным и максимальным элементами (не включая минимальный и
максимальный элементы).
"""


def change(arr, i):
    arr[i] = 0


while True:
    try:
        nums = []
        [nums.append(int(input(f'[{i}] = ')))
         for i in range(int(input('Введите длину списка: ')))]
        N = len(nums)

        [change(nums, nums.index(n))
         if nums.index(n) != nums.index(max(nums)) and nums.index(n) != nums.index(min(nums))
         else print(end='')
         for n in nums]

        print(nums)
        print()
    except ValueError:
        print("Вводите целые числа")
