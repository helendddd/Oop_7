#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from functools import partial


def update_label(value: int, label: tk.Label) -> None:
    """
    Обновляет текст метки в зависимости от выбранного radiobutton.
    """
    match value:
        case 1:
            text = "Первый"
        case 2:
            text = "Второй"
        case 3:
            text = "Третий"
        case _:
            text = "Неизвестный выбор"
    label.config(text=text)


if __name__ == "__main__":
    # Создание основного окна
    root = tk.Tk()
    root.title("Radiobutton без индикатора")

    # Фрейм для размещения radiobutton
    frame = tk.Frame(root)
    frame.pack(side="left", padx=10, pady=10)

    # Переменная для хранения выбранного значения
    var = tk.IntVar()
    var.set(1)  # Устанавливаем значение по умолчанию

    # Создание radiobutton
    radiobuttons = []
    for i in range(1, 4):
        rb = tk.Radiobutton(
            frame,
            text=str(i),
            value=i,
            width=10,
            height=5,
            indicatoron=False,  # Отключаем индикатор
            variable=var,
        )
        rb.pack(pady=5)
        radiobuttons.append(rb)

    # Метка для отображения выбранного значения
    label = tk.Label(root, text="Выберите кнопку", font=("Arial", 14))
    label.pack(side="left", anchor="center", fill="y", padx=30)

    # Привязка функции к radiobutton
    for rb in radiobuttons:
        rb.config(command=partial(update_label, rb["value"], label))

    # Запуск основного цикла обработки событий
    root.mainloop()
