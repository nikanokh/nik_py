"""
Приложение АБИТУРИЕНТ для автоматизации работы приемной комиссии,
которая обеспечивает обработку анкетных данных абитуриентов. Таблица Анкета
содержит следующие данные об абитуриентах: Регистрационный номер, Фамилия, Имя,
Отчество, Дата Рождения, Награды (наличие кр. Диплома или медали (да/нет)), Адрес,
выбранная Специальность.
"""

import sqlite3

conn = sqlite3.connect('students.db')
conn.execute('''CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY,
              name TEXT, 
              surname TEXT,
              birth TEXT,
              diploma INTEGER,
              address TEXT,
              speciality TEXT)''')
conn.close()


def execute_sql(sql, params=()):
    with sqlite3.connect('students.db') as conn:
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        return cursor.fetchall()


def print_students():
    students = execute_sql("SELECT * FROM students")
    for s in students:
        print(f"{s[0]}: {s[2]} {s[1]}, {s[3]}, {'Красный диплом' if s[4] else ''}, {s[5]}, {s[6]}")


def add_student():
    data = (
        input("ID: "),
        input("Имя: "),
        input("Фамилия: "),
        input("Дата рождения: "),
        1 if input("Красный диплом (да/нет)? ").lower() == 'да' else 0,
        input("Адрес: "),
        input("Специальность: ")
    )
    execute_sql("INSERT INTO students VALUES (?,?,?,?,?,?,?)", data)
    print("Добавлен!")


def delete_student():
    student_id = input("ID студента для удаления: ")
    execute_sql("DELETE FROM students WHERE id=?", (student_id,))
    print("Удален!")


def update_student():
    student_id = input("ID студента для изменения: ")
    field = input("Что меняем (name/surname/birth/diploma/address/speciality)? ")
    new_value = input("Новое значение: ")
    execute_sql(f"UPDATE students SET {field}=? WHERE id=?", (new_value, student_id))
    print("Обновлено!")


while True:
    print("\n1. Добавить \n2. Список \n3. Удалить \n4. Изменить \n5. Выход")
    choice = input("Выбор: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        print_students()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        break
