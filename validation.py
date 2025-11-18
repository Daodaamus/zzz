"""
Модуль валидации входных данных
"""

def validate_number(input_str):
    """Проверяет, является ли строка числом"""
    try:
        float(input_str)
        return True
    except ValueError:
        return False

def validate_operation(operation):
    """Проверяет корректность операции"""
    valid_operations = ['+', '-', '*', '/']
    return operation in valid_operations
