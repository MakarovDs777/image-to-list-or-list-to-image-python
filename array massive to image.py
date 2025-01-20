import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

def load_pixels_from_file(file_path):
    # Загружаем массив пикселей из текстового файла
    pixels = np.loadtxt(file_path, dtype=np.uint8)

    # Убеждаемся, что массив состоит из трех каналов
    if pixels.size % 3 != 0:
        raise ValueError("Размер массива пикселей должен быть кратен 3")

    # Определяем количество пикселей и вычисляем ширину и высоту (например, квдратное изображение)
    num_pixels = pixels.size // 3
    height = int(np.sqrt(num_pixels))
    width = num_pixels // height

    # Преобразуем в 3D массив (height, width, channels)
    return pixels.reshape((height, width, 3))

def save_image_from_pixels(pixels):
    # Проверяем, что массив имеет правильную форму
    if len(pixels.shape) != 3 or pixels.shape[2] != 3:
        raise ValueError("Массив должен иметь форму (высота, ширина, количество_цветовых_каналов)")

    # Создаем изображение из массива пикселей
    img = Image.fromarray(pixels)

    # Получаем путь к рабочему столу и сохраняем изображение
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    img.save(os.path.join(desktop_path, "image.png"))

def select_text_file():
    root = tk.Tk()
    root.withdraw()  # Скрываем корневое окно
    file_path = filedialog.askopenfilename(title="Выберите текстовый файл", filetypes=[("Text files", "*.txt")])
    
    if file_path:  # Проверяем, выбран ли файл
        pixels = load_pixels_from_file(file_path)
        save_image_from_pixels(pixels)
        print(f"Изображение сохранено на рабочем столе как 'image.png'")
    else:
        print("Файл не выбран.")

# Запуск диалогового окна
select_text_file()
