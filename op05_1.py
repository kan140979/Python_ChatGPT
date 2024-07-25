"""Задание 1: Базовая обработка исключений
Напиши функцию safe_divide, которая принимает два аргумента: a и b. Функция должна пытаться делить a на b и возвращать результат. Если произойдет ошибка деления на ноль (ZeroDivisionError), функция должна возвращать None вместо возникновения исключения. Продемонстрируй работу функции на нескольких примерах, включая деление на ноль."""

def safe_divide(a, b):
  try:
      result = a / b
      return result
  except ZeroDivisionError:
      return None

print(safe_divide(10, 2))  
print(safe_divide(10, 0))  
print(safe_divide(15, 3))  
print(safe_divide(5, 0))   
print(safe_divide(100, 25))  