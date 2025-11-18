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

def get_user_input():
    '''Получает ввод от пользователя'''
    return input('Введите операцию: ')

def get_user_input():
    '''Получает ввод от пользователя'''
    return input('Введите операцию: ')
