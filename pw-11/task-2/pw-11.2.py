"""
2. Из предложенного текстового файла (text18-2.txt) вывести на экран его содержимое,
количество знаков препинания. Сформировать новый файл, в который поместить текст в
стихотворной форме выведя строки в обратном порядке.
"""


import unicodedata


def is_punctuation_unicode(char):
    return unicodedata.category(char).startswith('P')


file = open('text18-2.txt', encoding='UTF-8')
data = file.read()
print(data)

sum_punctuation_marks = 0
for c in data:
    if is_punctuation_unicode(c):
        sum_punctuation_marks += 1

        # not (c.isalpha() or c.isdigit()) and c != '\n'

print('Количество знаков препинания: ' + str(sum_punctuation_marks))
file.close()

file = open('new.txt', 'w', encoding='UTF-8')
data_lines = data.splitlines()

string = ''
for c in data_lines[::-1]:
    string = string + c + '\n'

file.write(string)
