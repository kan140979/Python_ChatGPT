#Площадь прямоугольника. Написать программу, которая будет запрашивать у пользователя
#длину и ширину прямоугольника, а затем вычислять площадь.

# Запрашиваем у пользователя длину прямоугольника
length = float(input("Введите длину прямоугольника: "))

# Запрашиваем у пользователя ширину прямоугольника
width = float(input("Введите ширину прямоугольника: "))

# Вычисляем площадь прямоугольника
area = length * width

# Выводим результат
print(f"Площадь прямоугольника: {area}")
