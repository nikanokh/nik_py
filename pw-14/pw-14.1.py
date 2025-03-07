# \d{4}-\d{4}
# [А-Я][-а-яА-Я]+ [А-Я].[А-Я].
# «[-а-яА-Я ]+»

"""
Из текстового файла (writer.txt) выбрать фамилии писателей и годы жизни, а также
произведения ими написанные. Посчитать общее количество произведений в данном
файле.
"""

import re

file = open('writer.txt', 'r', encoding='UTF-8')
data = file.readlines()
count = 0

for line in data:
    try:
        first_name = re.findall(r'[А-Я][-а-яА-Я]+ [А-Я].[А-Я].', line)[0][:-5]
        years_of_life = re.findall(r'\d{4}-\d{4}', line)[0]
        compositions = re.findall(r'«[-а-яА-Я ]+»', line)
        count += len(compositions)

        print(first_name, years_of_life, compositions)

    except Exception:
        pass

print(f'Всего произведений: {count}')