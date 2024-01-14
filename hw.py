sample_list = [1, 'hello', True, 42, 'world', False]

'''Если x - число, то умножаем его на 2, иначе,
если x - строка, то конвертируем каждый символ в верхний регистр, 
иначе если x ложно, то возвращается True, иначе False'''

print(list(map(lambda x: x * 2 if type(x) is int else x.upper() if type(x) is str
               else not x, sample_list)))
