import random


# Функция для генерации случайной буквы
def random_letter():
    return chr(random.randint(65, 90))  # ASCII коды заглавных букв


# Функция для генерации случайной цифры
def random_digit():
    return str(random.randint(0, 9))


# Функция для генерации случайного знака препинания
def random_punctuation():
    punctuation_marks = ['!', '?', '.', ',', ';', ':', '-', '"', "'", ' ']
    return random.choice(punctuation_marks)


# Открываем файл в режиме записи бинарных данных
with open('random_data.bin', 'wb') as file:
    for i in range(100):  # Для примера генерируем 100 случайных символов
        random_choice = random.choice([random_letter, random_digit, random_punctuation])
        data = random_choice()
        # Записываем данные в файл
        file.write(data.encode('utf-8'))

# Открываем файл в режиме чтения бинарных данных
with open('random_data.bin', 'rb') as file:
    data = file.read().decode('utf-8')
    number_of_char = len(data)
    number_of_word = data.count(' ') + 1
    number_of_string = data.count('\n') + 1


print(f'Данные из файла:\n{data}\n\nСтатистика:\nЧисло символов: {number_of_char}'
      f'\nЧисло слов: {number_of_word}\nЧисло строк: {number_of_string}')