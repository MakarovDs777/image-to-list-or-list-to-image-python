import os
import numpy as np
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def image_to_text(output_file):
    """
    Преобразует выбранное изображение в текст и сохраняет его в файл.

    :param output_file: Имя выходного текстового файла
    """
    # Открыть окно для выбора изображения
    Tk().withdraw()  # Скрыть основное окно
    image_path = askopenfilename(title='Выберите изображение', filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

    if image_path:
        img = Image.open(image_path).convert('L')  # Преобразование в градации серого
        img_array = np.array(img)

        with open(output_file, 'w') as f:
            for row in img_array:
                line = ''.join([str(pixel // 25) for pixel in row])  # Нормализация градаций к числам от 0 до 9
                f.write(line + '\n')

        print(f"Image text saved as {output_file}")
    else:
        print("Изображение не выбрано.")

# Пример использования
output_file = os.path.join(os.path.expanduser("~"), "Desktop", "image_text.txt")
image_to_text(output_file)