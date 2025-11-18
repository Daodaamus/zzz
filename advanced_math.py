"""
Расширенные математические операции
"""

import math

def power(base, exponent):
    """Возведение в степень"""
    return base ** exponent

def square_root(number):
    """Квадратный корень"""
    if number < 0:
        raise ValueError("Квадратный корень из отрицательного числа!")
    return math.sqrt(number)

def factorial(n):
    """Факториал числа"""
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен!")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def logarithm(number, base=10):
    """Логарифм числа"""
    if number <= 0:
        raise ValueError("Логарифм определен только для положительных чисел!")
    return math.log(number, base)
