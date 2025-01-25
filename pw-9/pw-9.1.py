"""
Дана строка «Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4». Преобразовать
информацию из строки в словарь, найти среднее арифметическое оценок,
результаты вывести на экран.
"""

data = "Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4"
data_parts = data.split()

marks_str = data_parts[3:]
marks = [int(mark) for mark in marks_str]

average_marks = sum(marks) / len(marks)

student_info = {
    "first_name": data_parts[0],
    "name": data_parts[1],
    "group": data_parts[2],
    "marks": marks,
    "average_marks": average_marks
}

print(student_info)
