"""
Дано целое число A. Проверить истинность высказывания: «Число A является
нечетным».
"""

import tkinter as tk
from tkinter import messagebox


def check_odd_number():
    try:
        a = int(entry.get())
        if a % 2 == 1:
            messagebox.showinfo("Результат", f"Число {a} является нечетным")
        else:
            messagebox.showinfo("Результат", f"Число {a} является четным")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целое число")


root = tk.Tk()
root.title("Проверка нечетности числа")
root.geometry("300x150")

label = tk.Label(root, text="Введите целое число A:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

check_button = tk.Button(root, text="Проверить", command=check_odd_number)
check_button.pack(pady=10)

root.mainloop()