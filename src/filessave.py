#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tkinter as tk


def check_file(file_name: str) -> str:
    if "/" in file_name:
        return file_name
    return "TXT/" + file_name


def open_file(file_name: str, textbox: tk.Text) -> None:
    file_name = check_file(file_name)
    if not os.path.exists(file_name):
        textbox.delete("1.0", "end")
        textbox.insert("1.0", "Файл не найден")
        return
    try:
        with open(file_name, "r", encoding="utf8") as fin:
            text = fin.read()
            textbox.delete("1.0", "end")
            textbox.insert("1.0", text)
    except Exception as e:
        textbox.delete("1.0", "end")
        textbox.insert("1.0", "Ошибка при открытии файла\n" + str(e))


def save_file(file_name: str, textbox: tk.Text) -> None:
    file_name = check_file(file_name)
    try:
        with open(file_name, "w", encoding="utf8") as fout:
            text = textbox.get("1.0", "end")
            fout.write(text)
    except Exception as e:
        textbox.delete("1.0", "end")
        textbox.insert("1.0", "Ошибка при сохранении файла\n" + str(e))


if __name__ == "__main__":
    root = tk.Tk()
    f1 = tk.Frame(root)
    f1.pack()
    f2 = tk.Frame(root)
    f2.pack()
    f3 = tk.Frame(f2)
    f3.pack()
    textbox = tk.Text(f3, width=50, height=30, wrap="none")
    textbox.pack(side="left")
    entry = tk.Entry(f1, width=30)
    entry.pack(side="left", padx=10, pady=10)
    but_open = tk.Button(
        f1, text="Открыть", command=lambda: open_file(entry.get(), textbox)
    )
    but_open.pack(side="left", padx=10, pady=5)
    but_save = tk.Button(
        f1, text="Сохранить", command=lambda: save_file(entry.get(), textbox)
    )
    but_save.pack(side="left", padx=10, pady=5)
    scroll_y = tk.Scrollbar(f3, command=textbox.yview)
    scroll_y.pack(side="left", fill="y")
    textbox.config(yscrollcommand=scroll_y.set)
    scroll_x = tk.Scrollbar(f2, command=textbox.xview, orient="horizontal")
    scroll_x.pack(fill="x")
    textbox.config(xscrollcommand=scroll_x.set)
    root.mainloop()
