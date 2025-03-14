import os
from PIL import Image
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def text_to_image():
    """
    Преобразует текстовый файл обратно в изображение.
    """
    # Открыть окно для выбора текстового файла
    Tk().withdraw()  # Скрыть основное окно
    input_file = askopenfilename(title='Выберите текстовый файл', filetypes=[("Text files", "*.txt")])
    
    if input_file:
        output_image_path = asksaveasfilename(title='Сохранить изображение как', defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        
        if output_image_path:
            with open(input_file, 'r') as f:
                lines = f.readlines()

            # Определить размеры изображения
            height = len(lines)
            width = max(len(line.strip()) for line in lines)
            img_array = np.zeros((height, width), dtype=np.uint8)
            
            for i, line in enumerate(lines):
                for j, char in enumerate(line.strip()):
                    img_array[i][j] = int(char) * 25  # Восстановление градаций по умолчанию

            img = Image.fromarray(img_array)
            img.save(output_image_path)
            print(f"Reconstructed image saved as {output_image_path}")
        else:
            print("Изображение не сохранено.")
    else:
        print("Текстовый файл не выбран.")

# Пример использования
text_to_image()