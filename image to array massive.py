import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog

def select_image_file():
    root = tk.Tk()
    root.withdraw()  # Скрываем корневое окно
    file_path = filedialog.askopenfilename(title="Выберите файл изображения", filetypes=[("Image files", ".jpg;.jpeg;.png;.bmp")])
    if file_path:  # Проверяем, выбран ли файл
        image = Image.open(file_path)
        pixels = np.array(image)
        print(pixels)
    else:
        print("Файл не выбран.")

# Запуск диалогового окна
select_image_file()
