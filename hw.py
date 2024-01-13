
years = [i for i in range(1950, 2025)] # генератор списка, годы с 1950 по 2024


# Лямбда функция проверяет, является ли год високосным

print(list(filter(lambda y: y % 4 == 0 or y % 400 == 0 and y % 100 != 0, years)))
