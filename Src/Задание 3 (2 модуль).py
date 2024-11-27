from PIL import Image
import os

def join_images(image_paths, output_path):
    """Склеивает изображения горизонтально."""
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

        new_im.save(output_path)
        print(f"Изображения склеены и сохранены как {output_path}")
        return output_path  # Возвращаем путь к сохраненному изображению

    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден: {e}")
        return None
    except Exception as e:
        print(f"Произошла ошибка при склеивании: {e}")
        return None


def get_image_paths_from_user():
    """Получает пути к двум изображениям от пользователя."""
    while True:
        try:
            path1 = input("Введите полный путь к первому изображению: ")
            path2 = input("Введите полный путь ко второму изображению: ")
            if not (os.path.exists(path1) and os.path.exists(path2)):
                raise FileNotFoundError("Один или оба файла не найдены.")
            return path1, path2
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(f"Ошибка ввода: {e}")


if __name__ == "__main__":
    path1, path2 = get_image_paths_from_user()
    
    # Извлекаем имя файла без расширения для первого изображения
    base_name1 = os.path.splitext(os.path.basename(path1))[0]
    #Извлекаем директорию для сохранения
    directory = os.path.dirname(path1)
    
    output_path = os.path.join(directory, f"{base_name1}_joined.jpg")  # путь к результату
    result_path = join_images([path1, path2], output_path)

    if result_path:
        print(f"Склеенное изображение сохранено по пути: {result_path}")