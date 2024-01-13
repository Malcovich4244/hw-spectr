from functools import reduce


list_1 = ['Hello', 'World', 'Python', 'is', 'great!']

print(reduce(lambda a, b: (a + ' ' + b).lower(), list_1))
