"""
Задание №2

Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""

def fibonacci_even_sum(number_max:int) -> int:
    """Возвращает сумму всех чётных чисел ряда Фибоначчи, не превышающих 4 миллиона."""
    number_first = 1
    number_second = 2
    number_sum = 0

    while number_first <= number_max:
        if number_first % 2 == 0:
            number_sum += number_first

        number_temp = number_first
        number_first = number_second
        number_second = number_temp + number_second

    return number_sum


if __name__ == "__main__":
    result = fibonacci_even_sum(4000000)
    print(result)  # Ожидаемый ответ: 4613732
