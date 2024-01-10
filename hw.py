import os


def display_folder_structure(path, indent=''):
    if os.path.isfile(path):  # Если путь - файл
        print(f'{indent + os.path.basename(path)} - {str(os.path.getsize(path))} bytes')  # выводим имя и размер файла
    else:  # Если путь - папка
        print(f'{indent + os.path.basename(path)} /')  # выводим имя папки
        for item in os.listdir(path):  # проходим по всем элементам в папке
            item_path = os.path.join(path, item)  # получаем полный путь к элементу
            if os.path.isfile(item_path):  # Если элемент - файл
                print(f'{indent}  {item} - {str(os.path.getsize(item_path))} bytes')  # выводим имя и размер файла
            elif os.path.isdir(item_path):  # Если элемент - папка
                print(f'{indent}  {item}')  # выводим имя папки
                display_folder_structure(item_path, indent + "    ")  # вызываем рекурсивно эту же функцию для подпапки


folder_path = 'полный/путь/к/папке'  # замените на полный путь к нужной папке
display_folder_structure(folder_path)  # вызываем функцию для отображения структуры папки
