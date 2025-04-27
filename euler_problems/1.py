"""
Задание №1

Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9.
Сумма этих чисел равна 23. Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""

def find_sum_multiples(divisor1: int, divisor2: int, limit: int) -> int:
    """Возвращает сумму всех чисел меньше limit, которые кратны divisor1 или divisor2."""
    total_sum = 0
    for i in range(limit):
        if i % divisor1 == 0 or i % divisor2 == 0:
            total_sum += i
    return total_sum


if __name__ == "__main__":
    result = find_sum_multiples(3, 5, 1000)
    print(result)  # Ожидаемый результат: 233168
