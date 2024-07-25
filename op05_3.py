"""Задание 3: Обработка исключений прошлых программ
Возьми одну из программ, которую мы писали на прошлых уроках, продумай, какие ошибки в программе могут появляться(можно прям специально пробовать ее ломать) и дополни код конструкцией try-except для обработки выявленных исключений."""


"""Проверка на четность чисел в диапазоне: Напишите программу, которая принимает от
пользователя два числа (начало и конец диапазона) и выводит все четные числа в этом
диапазоне с помощью цикла for"""

try:
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))

    if start > end:
        print(
            "Ошибка: Начало диапазона должно быть меньше или равно концу диапазона."
        )
    else:
        print("Четные числа в диапазоне от", start, "до", end, ":")

        for number in range(start, end + 1):
            if number % 2 == 0:  
               print(number)
except ValueError:
    print("Вы ввели некорректные данные.")




