#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk


def on_label_click(color_code, color_name):
    entry.delete(0, tk.END)
    entry.insert(0, color_code)
    label.config(text=color_name)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Цвета радуги")

    root.geometry("200x400")

    entry = tk.Entry(root, width=20, font=("Arial", 14))
    entry.pack(pady=10)

    label = tk.Label(root, text="", font=("Arial", 14))
    label.pack(pady=10)

    colors = [
        ("#ff0000", "Красный"),
        ("#ff7d00", "Оранжевый"),
        ("#ffff00", "Желтый"),
        ("#00ff00", "Зеленый"),
        ("#007dff", "Голубой"),
        ("#0000ff", "Синий"),
        ("#7d00ff", "Фиолетовый")
    ]

    for color_code, color_name in colors:
        color_label = tk.Label(
            root,
            bg=color_code,
            width=20,
            height=2,
        )

        color_label.bind(
            "<Button-1>",
            lambda e,
            code=color_code,
            name=color_name: on_label_click(code, name)
            )
        color_label.pack(pady=5)

    root.mainloop()
