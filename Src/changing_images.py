from PIL import Image
import os

def resize_image(input_path, output_path, new_width, new_height):

    try:
        img = Image.open(input_path)
        img = img.resize((new_width, new_height), Image.LANCZOS)  # LANCZOS для высокого качества
        img.save(output_path)
        print(f"Изображение {input_path} изменено и сохранено как {output_path}")
    except FileNotFoundError:
        print(f"Ошибка: Файл {input_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка при изменении размера: {e}")


def join_images(image_paths, output_path):
    
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

    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден: {e}")
    except Exception as e:
        print(f"Произошла ошибка при склеивании: {e}")


if __name__ == "__main__":
    resize_image("image1.jpg", "image1_resized.jpg", 200, 150)  
    image_paths = ["image1_resized.jpg", "image2.jpg"]  
    output_path = "joined_image.jpg"
    join_images(image_paths, output_path)