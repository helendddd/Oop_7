#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk


def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2

        result_label.config(text=f"Результат: {result}")
    except (ValueError, ZeroDivisionError):
        result_label.config(text="Ошибка")


if __name__ == "__main__":
    # Создание основного окна
    root = tk.Tk()
    root.title("Калькулятор")

    # Текстовые поля для ввода чисел
    entry1 = tk.Entry(root, width=20)
    entry1.pack(pady=5)

    entry2 = tk.Entry(root, width=20)
    entry2.pack(pady=5)

    # Кнопки для операций
    button_add = tk.Button(root, text="+", command=lambda: calculate("+"))
    button_add.pack(side=tk.LEFT, padx=5)

    button_sub = tk.Button(root, text="-", command=lambda: calculate("-"))
    button_sub.pack(side=tk.LEFT, padx=5)

    button_mul = tk.Button(root, text="*", command=lambda: calculate("*"))
    button_mul.pack(side=tk.LEFT, padx=5)

    button_div = tk.Button(root, text="/", command=lambda: calculate("/"))
    button_div.pack(side=tk.LEFT, padx=5)

    # Метка для отображения результата
    result_label = tk.Label(root, text="Результат: ")
    result_label.pack(pady=10)

    # Запуск основного цикла обработки событий
    root.mainloop()
