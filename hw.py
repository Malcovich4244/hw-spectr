
def fibonachi_numbers(max_lenth: int) -> list:
    # Генератор для чисел Фибоначчи до определенного предела
    a, b = 0, 1
    while b <= max_lenth:
        # Пока текущее число не превысило предел, возвращаем его в качестве следующего числа
        yield b
        a, b = b, a + b


print(*fibonachi_numbers(100))


class FibonachiNumbers:
    def __init__(self, max_lenth: int) -> None:
        self.a = 0
        self.b = 1
        self.max_lenth = max_lenth

    def __iter__(self) -> None:
        # Возвращаем сам объект в качестве итератора
        return self

    def __next__(self) -> int:
        # Генерируем следующее число Фибоначчи до достижения предела
        if self.b > self.max_lenth:
            raise StopIteration
        else:
            result = self.b
            self.a, self.b = self.b, self.a + self.b
        return result


print(*FibonachiNumbers(100))
