#Создать калькулятор — программу, в которой мы вводим 2 числа, и с ними производятся
#сразу все математические действия, рассмотренные в уроке.


def calculator():
    # Ввод двух чисел
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    # Выполнение математических операций
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2

    # Обработка деления с проверкой на деление на ноль
    if num2 != 0:
        division_result = num1 / num2
        integer_division_result = num1 // num2
        remainder_result = num1 % num2
    else:
        division_result = "Ошибка: деление на ноль"
        integer_division_result = "Ошибка: деление на ноль"
        remainder_result = "Ошибка: деление на ноль"

    power_result = num1**num2

    # Вывод результатов
    print(f"Сумма: {sum_result}")
    print(f"Разность: {difference_result}")
    print(f"Произведение: {product_result}")
    print(f"Частное: {division_result}")
    print(f"Целая часть от деления: {integer_division_result}")
    print(f"Остаток от деления: {remainder_result}")
    print(f"{num1} в степени {num2}: {power_result}")


# Запуск калькулятора
calculator()
