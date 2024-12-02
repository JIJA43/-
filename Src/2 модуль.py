from PIL import Image, UnidentifiedImageError  # Импортируем необходимые классы
import os

def join_images(image_paths):
    """Склеивает изображения горизонтально и возвращает путь к сохраненному файлу."""
    try:
        images = [Image.open(path) for path in image_paths]
        widths, heights = zip(*(i.size for i in images))

        total_width = sum(widths)
        max_height = max(heights)

        new_im = Image.new('RGB', (total_width, max_height))

        x_offset = 0
        for im in images:
            new_im.paste(im, (x_offset, 0))
            x_offset += im.size[0]

        # Извлекаем имя файла без расширения для первого изображения
        base_name1 = os.path.splitext(os.path.basename(image_paths[0]))[0]
        # Извлекаем директорию для сохранения
        directory = os.path.dirname(image_paths[0])
        output_path = os.path.join(directory, f"{base_name1}_joined.jpg")
        new_im.save(output_path)
        print(f"Изображения склеены и сохранены как {output_path}")
        return output_path

    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден: {e}")
        return None
    except UnidentifiedImageError:
        print("Ошибка: Не удалось открыть один из файлов как изображение.")
        return None
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return None

def get_image_paths_from_user():
    """Получает пути к изображениям от пользователя."""
    while True:
        try:
            path1 = input("Введите полный путь к первому изображению: ")
            path2 = input("Введите полный путь ко второму изображению: ")
            if not (os.path.exists(path1) and os.path.exists(path2)):
                raise FileNotFoundError("Один или оба файла не найдены.")
            return [path1, path2]  # Возвращаем список путей
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(f"Ошибка ввода: {e}")
if __name__ == "__main__":  # Исправлено условие
    image_paths = get_image_paths_from_user()
    if image_paths:
        result_path = join_images(image_paths)
        if result_path:
            print(f"Склеенное изображение сохранено по пути: {result_path}")
