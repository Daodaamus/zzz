"""
Основной модуль калькулятора - ВЕРСИЯ A
"""

from validation import get_valid_number, get_valid_operation

def add(a, b):
    """Сложение двух чисел - Версия A"""
    print("Выполняется сложение...")
    return a + b

def subtract(a, b):
    """Вычитание двух чисел - Версия A"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел - Версия A"""
    return a * b

def divide(a, b):
    """Деление двух чисел - Версия A"""
    if b == 0:
        raise ValueError("На ноль делить нельзя!")
    return a / b

def main():
    """Основная функция - Версия A"""
    print("=== КАЛЬКУЛЯТОР ===")
    a = get_valid_number("Первое число: ")
    b = get_valid_number("Второе число: ")
    operation = get_valid_operation("Операция (+, -, *, /): ")
    
    if operation == '+':
        result = add(a, b)
    elif operation == '-':
        result = subtract(a, b)
    elif operation == '*':
        result = multiply(a, b)
    elif operation == '/':
        result = divide(a, b)
    
    print(f"Ответ: {result}")

if __name__ == "__main__":
    main()
