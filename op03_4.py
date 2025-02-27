#Проверка на четность чисел в диапазоне: Напишите программу, которая принимает от
#пользователя два числа (начало и конец диапазона) и выводит все четные числа в этом
#диапазоне с помощью цикла for

# Запрашиваем у пользователя ввод начала и конца диапазона
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

# Проверяем, чтобы начало не было больше конца
if start > end:
    print(
        "Ошибка: Начало диапазона должно быть меньше или равно концу диапазона."
    )
else:
    print("Четные числа в диапазоне от", start, "до", end, ":")

    # Проходим по числам в заданном диапазоне
    for number in range(start, end + 1):
        if number % 2 == 0:  # Проверяем, является ли число четным
            print(number)
