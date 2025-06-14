"""
В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
приближенный к оригиналу (см. таблицу 1).
"""


import tkinter as tk
from tkinter import ttk, messagebox


def submit_form():
    if not name_entry.get():
        messagebox.showerror("Ошибка", "Поле 'Имя' обязательно")
        return
    if not email_entry.get():
        messagebox.showerror("Ошибка", "Поле 'Email' обязательно")
        return
    if not age_entry.get():
        messagebox.showerror("Ошибка", "Поле 'Возраст' обязательно")
        return
    try:
        age = int(age_entry.get())
        if age < 18 or age > 70:
            messagebox.showerror("Ошибка", "Возраст 18-70")
            return
    except ValueError:
        messagebox.showerror("Ошибка", "Возраст должен быть числом")
        return

    selected_animals = [animals[i] for i, var in enumerate(animal_vars) if var.get()]
    data = {
        "Имя": name_entry.get(),
        "Телефон": phone_entry.get(),
        "Email": email_entry.get(),
        "Возраст": age_entry.get(),
        "Пол": gender_combobox.get(),
        "Личные качества": qualities_text.get("1.0", tk.END).strip(),
        "Животные": selected_animals
    }
    messagebox.showinfo("Успех", "Заявка отправлена!")
    print("Данные:", data)

root = tk.Tk()
root.title("Форма заявки в зоопарк")
root.geometry("500x650")

tk.Label(root, text="Форма заявки в зоопарк", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(root, text="Обязательные поля помечены *", font=("Arial", 10)).pack(pady=5)

contact_frame = tk.LabelFrame(root, text="Контактная информация")
contact_frame.pack(fill=tk.X, padx=10, pady=5)

tk.Label(contact_frame, text="Имя *").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(contact_frame, width=40)
name_entry.grid(row=0, column=1)

tk.Label(contact_frame, text="Телефон").grid(row=1, column=0, sticky="w")
phone_entry = tk.Entry(contact_frame, width=40)
phone_entry.grid(row=1, column=1)

tk.Label(contact_frame, text="Email *").grid(row=2, column=0, sticky="w")
email_entry = tk.Entry(contact_frame, width=40)
email_entry.grid(row=2, column=1)

personal_frame = tk.LabelFrame(root, text="Персональная информация")
personal_frame.pack(fill=tk.X, padx=10, pady=5)

tk.Label(personal_frame, text="Возраст*").grid(row=0, column=0, sticky="w")
age_entry = tk.Entry(personal_frame, width=10)
age_entry.grid(row=0, column=1, sticky="w")

tk.Label(personal_frame, text="Пол").grid(row=0, column=2, sticky="w", padx=10)
gender_combobox = ttk.Combobox(personal_frame, values=["Женщина", "Мужчина"], width=8, state="readonly")
gender_combobox.set("Женщина")
gender_combobox.grid(row=0, column=3)

tk.Label(personal_frame, text="Личные качества").grid(row=1, column=0, sticky="nw")
qualities_text = tk.Text(personal_frame, width=40, height=5)
qualities_text.grid(row=2, column=0, columnspan=4)

animals_frame = tk.LabelFrame(root, text="Любимые животные")
animals_frame.pack(fill=tk.X, padx=10, pady=5)

animals = ["Зебра", "Кошак", "Анаконда", "Человек", "Слон", "Антилопа", "Голубь", "Краб"]
animal_vars = []
for i, animal in enumerate(animals):
    var = tk.BooleanVar()
    animal_vars.append(var)
    tk.Checkbutton(animals_frame, text=animal, variable=var).grid(row=i//4, column=i%4, sticky="w")

tk.Button(root, text="Отправить", command=submit_form, bg="lightblue").pack(pady=20)

root.mainloop()