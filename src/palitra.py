#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk


def on_label_click(color_code, color_name):
    entry.delete(0, tk.END)  # Очищаем текстовое поле
    entry.insert(0, color_code)  # Вставляем код цвета
    label.config(text=color_name)  # Обновляем метку с названием цвета


if __name__ == "__main__":
    # Создание основного окна
    root = tk.Tk()
    root.title("Цвета радуги")

    # Устанавливаем размер окна
    root.geometry("600x200")

    # Текстовое поле для вывода кода цвета
    entry = tk.Entry(root, width=20, font=("Arial", 14))
    entry.pack(pady=10)

    # Метка для вывода названия цвета
    label = tk.Label(root, text="", font=("Arial", 14))
    label.pack(pady=10)

    # Цвета радуги и их коды
    colors = [
        ("#ff0000", "Красный"),
        ("#ff7d00", "Оранжевый"),
        ("#ffff00", "Желтый"),
        ("#00ff00", "Зеленый"),
        ("#007dff", "Голубой"),
        ("#0000ff", "Синий"),
        ("#7d00ff", "Фиолетовый")
    ]

    # Фрейм для горизонтального расположения цветных меток
    frame = tk.Frame(root)
    frame.pack()

    # Создание цветных меток (вместо кнопок)
    for color_code, color_name in colors:
        color_label = tk.Label(
            frame,
            bg=color_code,  # Цвет фона метки
            width=6,  # Ширина метки
            height=3,  # Высота метки
        )

        color_label.bind(
            "<Button-1>",
            lambda e,
            code=color_code,
            name=color_name: on_label_click(code, name)
            )
        color_label.pack(side="left", padx=5, pady=5)

    root.mainloop()
