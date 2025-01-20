import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

def select_image_file():
    root = tk.Tk()
    root.withdraw()  # Скрываем корневое окно
    file_path = filedialog.askopenfilename(title="Выберите файл изображения", filetypes=[("Image files", ".jpg;.jpeg;.png;.bmp")])
    
    if file_path:  # Проверяем, выбран ли файл
        image = Image.open(file_path)
        pixels = np.array(image)
        np.set_printoptions(threshold=np.inf)  # Выводим все элементы массива
        
        # Печать массива в консоль
        # print(pixels)
        
        # Сохранение массива в текстовый файл на рабочий стол
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        text_file_path = os.path.join(desktop_path, "pixels_array.txt")
        
        np.savetxt(text_file_path, pixels.reshape(-1, pixels.shape[2]), fmt='%d')  # Сохраняем массив в текстовый файл
        print(f"Массив сохранен в {text_file_path}")
    else:
        print("Файл не выбран.")

# Запуск диалогового окна
select_image_file()
