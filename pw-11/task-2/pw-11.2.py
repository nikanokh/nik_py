"""
2. Из предложенного текстового файла (text18-2.txt) вывести на экран его содержимое,
количество знаков препинания. Сформировать новый файл, в который поместить текст в
стихотворной форме выведя строки в обратном порядке.
"""

file = open('text18-2.txt', encoding='UTF-8')
data = file.read()
print(data)

sum_punctuation_marks = 0
for c in data:
    if c == '.' or ',' or ':' or ';' or '!' or '?':
        sum_punctuation_marks += 1

file.close()

file = open('new.txt', 'w', encoding='UTF-8')
data_lines = data.splitlines()

string = ''
for c in data_lines[::-1]:
    string = string + c + '\n'

file.write(string)
