import numpy as np
from PIL import Image
import os

def save_image_from_pixels(pixels):
    # Проверяем, что входные данные являются numpy-массивом
    if not isinstance(pixels, np.ndarray):
        raise ValueError("Входные данные должны быть numpy-массивом")

    # Проверяем, что массив имеет правильную форму
    if len(pixels.shape) != 3 or pixels.shape[2] not in [3, 4]:
        raise ValueError("Массив должен иметь форму (высота, ширина, количество_цветовых_каналов)")

    # Создаем изображение из массива пикселей
    img = Image.fromarray(pixels.astype(np.uint8))

    # Получаем путь к рабочему столу
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    img.save(os.path.join(desktop_path, "image.png"))

# Пример использования
pixels = np.random.randint(0, 256, size=(512, 512, 3), dtype=np.uint8)
save_image_from_pixels(pixels)
