import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

def select_image_file():
    file_path = filedialog.askopenfilename(title="Выберите файл изображения", filetypes=[("Image files", ".jpg;.jpeg;.png;.bmp")])
    
    if file_path:  # Проверяем, выбран ли файл
        image = Image.open(file_path)
        pixels = np.array(image)
        np.set_printoptions(threshold=np.inf)  # Выводим все элементы массива
        
        # Сохранение массива в текстовый файл на рабочий стол
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        text_file_path = os.path.join(desktop_path, "pixels_array.txt")
        np.savetxt(text_file_path, pixels.reshape(-1, pixels.shape[2]), fmt='%d')  # Сохраняем массив в текстовый файл
        print(f"Массив сохранен в {text_file_path}")
    else:
        print("Файл не выбран.")

def load_pixels_from_file(file_path):
    pixels = np.loadtxt(file_path, dtype=np.uint8)

    print("Размер загруженного массива:", pixels.size)
    
    # Проверим содержание
    print("Содержимое массива перед reshaping:", pixels)

    if pixels.size % 3 != 0:
        raise ValueError("Размер массива пикселей должен быть кратен 3")

    num_pixels = pixels.size // 3

    height = int(np.sqrt(num_pixels))
    width = (num_pixels + height - 1) // height

    expected_size = height * width * 3
    if expected_size > pixels.size:
        num_pixels = pixels.size // 3
        height = (num_pixels + width - 1) // width

    total_elements = height * width * 3
    if total_elements != pixels.size:
        print("Недостаточно данных для формирования правильного изображения.")
        return None

    reshaped_pixels = pixels.reshape((height, width, 3))
    print(f"Форма массива после reshaping: {reshaped_pixels.shape}")

    return reshaped_pixels

def save_image_from_pixels(pixels):
    if len(pixels.shape) != 3 or pixels.shape[2] != 3:
        raise ValueError("Массив должен иметь форму (высота, ширина, количество_цветовых_каналов)")

    img = Image.fromarray(pixels)
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    img.save(os.path.join(desktop_path, "image.png"))

def select_text_file():
    file_path = filedialog.askopenfilename(title="Выберите текстовый файл", filetypes=[("Text files", "*.txt")])
    
    if file_path:  # Проверяем, выбран ли файл
        pixels = load_pixels_from_file(file_path)
        if pixels is None:
            print("Ошибка при загрузке изображения.")
            return
        save_image_from_pixels(pixels)
        print(f"Изображение сохранено на рабочем столе как 'image.png'")
    else:
        print("Файл не выбран.")

def main():
    root = tk.Tk()
    root.geometry("450x350")

    # Кнопка для конвертации изображения в массив
    button_image_to_array = tk.Button(root, text="Картинку в текст", command=select_image_file)
    button_image_to_array.pack(pady=20)

    # Кнопка для конвертации текста в изображение
    button_array_to_image = tk.Button(root, text="Текст в картинку", command=select_text_file)
    button_array_to_image.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
