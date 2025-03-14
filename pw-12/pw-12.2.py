"""
Составить список, в который будут включены только согласные буквы и
привести их к верхнему регистру. Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль',
'Дели', 'Каир'].
"""

words = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}


def filter_vowels(char):
    return char.lower() not in vowels


nlist = list(
      map(
            lambda string: ''.join([str(c).upper() for c in string if filter_vowels(c)]),
            [word for word in words]
      )
)

print(nlist)
