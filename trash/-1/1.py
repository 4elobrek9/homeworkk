# -*- coding: utf-8 -*-

import tkinter as tk
import os
import subprocess

def open_console():
    # Получаем путь к директории, где находится файл
    current_directory = os.path.dirname(os.path.abspath(__file__))

    if os.name == 'nt':  # Если ОС Windows
        subprocess.Popen(['cmd.exe', '/K', f'cd {current_directory}'])
    else:  # Для Unix-подобных систем (Linux, macOS)
        subprocess.Popen(['gnome-terminal', '--working-directory', current_directory])

def change_font():
    global current_font_index
    current_font_index = (current_font_index + 1) % len(fonts)
    label.config(font=fonts[current_font_index])

# Создание главного окна
root = tk.Tk()
root.title("quest 1")

# Фиксируем размер окна
root.geometry("552x228")  # Устанавливаем начальный размер окна
root.resizable(True, False)  # Запрещаем изменение размера окна

# Список шрифтов
fonts = [
    ("Helvetica", 16),
    ("Arial", 20),
    ("Times New Roman", 24),
    ("Courier New", 18),
    ("Comic Sans MS", 22),
]

current_font_index = 0
label = tk.Label(root, text="Dont compare yourself with anyone in this world...\n"
        "if you do so, you are insulting yourself.", font=fonts[current_font_index])
label.pack(pady=20)

button = tk.Button(root, text="change", command=change_font)
button.pack(pady=10)

console_button = tk.Button(root, text="open cmd", command=open_console)
console_button.pack(pady=10)


# Запуск основного цикла
root.mainloop()

