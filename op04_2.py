#Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 #значения (с помощью кортежа, после return перечислить все значения через запятую): #периметр квадрата, площадь квадрата и диагональ квадрата.

import math

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side
    return perimeter, area, diagonal

# Пример использования функции
side_length = 5
perimeter, area, diagonal = square(side_length)
print(f"Периметр: {perimeter}, Площадь: {area}, Диагональ: {diagonal}")