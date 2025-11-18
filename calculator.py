"""
Основной модуль калькулятора - РАЗРЕШЕННАЯ ВЕРСИЯ
"""

from validation import get_valid_number, get_valid_operation

def add(a, b):
    """Сложение двух чисел"""
    print("Выполняется сложение...")
    return a + b

def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление двух чисел"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно!")
    return a / b

def main():
    """Основная функция калькулятора"""
    print("=== КАЛЬКУЛЯТОР v2.0 ===")
    print("-----------------------")
    
    a = get_valid_number("Введите первое число: ")
    b = get_valid_number("Введите второе число: ")
    operation = get_valid_operation("Выберите операцию (+, -, *, /): ")
    
    if operation == '+':
        result = add(a, b)
    elif operation == '-':
        result = subtract(a, b)
    elif operation == '*':
        result = multiply(a, b)
    elif operation == '/':
        result = divide(a, b)
    
    print(f"Результат вычисления: {result}")

if __name__ == "__main__":
    main()
